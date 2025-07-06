import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from vectorstore_loader import load_vectorstore
from llm_config import load_llm
from tools import build_tool

def test_tool_execution():
    vs = load_vectorstore("vs_data1")
    llm = load_llm()
    tool = build_tool("WHO_Tool", "Test WHO tool", vs, llm)

    response = tool.func("What is amoxicillin used for?")
    assert isinstance(response, str)
    assert len(response) > 10
