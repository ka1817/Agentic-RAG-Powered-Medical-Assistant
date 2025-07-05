# src/vectorstore_loader.py

import os
from langchain_huggingface.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS

def load_vectorstore(name: str):
    """Loads a FAISS vectorstore from disk."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    path = os.path.join(base_dir, "vectorstores", name)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    return FAISS.load_local(path, embeddings, allow_dangerous_deserialization=True)
