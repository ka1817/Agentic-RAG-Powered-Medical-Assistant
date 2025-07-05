# src/llm_config.py

import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

def load_llm():
    """Initializes and returns the LLM."""
    load_dotenv()
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise ValueError("GROQ_API_KEY not found in .env file")

    llm = ChatGroq(api_key=api_key, model="llama-3.3-70b-versatile")
    return llm
