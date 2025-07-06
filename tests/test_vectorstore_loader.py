import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from vectorstore_loader import load_vectorstore

def test_vectorstore_loading():
    vs = load_vectorstore("vs_data1")
    results = vs.similarity_search("paracetamol", k=1)
    assert len(results) > 0
