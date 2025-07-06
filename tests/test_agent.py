import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from agent import get_agent

def test_agent_invocation():
    agent = get_agent()
    question = "What cancer drugs are used in childhood leukemia?"
    result = agent.invoke(question)

    assert isinstance(result, dict)
    assert "output" in result
    assert len(result["output"]) > 10
