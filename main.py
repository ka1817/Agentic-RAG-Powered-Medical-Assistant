from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from agent import get_agent 

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

agent = get_agent()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "response": ""})

@app.post("/", response_class=HTMLResponse)
async def ask_question(request: Request, question: str = Form(...)):
    try:
        result = agent.invoke(question)
        final_answer = result["output"] if isinstance(result, dict) and "output" in result else str(result)
    except Exception as e:
        final_answer = f"❌ Error: {str(e)}"
    return templates.TemplateResponse("index.html", {"request": request, "response": final_answer})
