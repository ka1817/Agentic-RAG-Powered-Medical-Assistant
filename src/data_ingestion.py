# src/data_ingestion.py

import os
from langchain_community.document_loaders import DirectoryLoader, UnstructuredFileLoader

def load_WHO_pdf_documents():
    """Loads WHO PDF documents from data_rag1."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "data1")
    loader = DirectoryLoader(data_path, glob="**/*.pdf", loader_cls=UnstructuredFileLoader)
    return loader.load()

def load_oncology_pdf_documents():
    """Loads Oncology Handbook PDF documents from data_rag2."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "..", "data", "data2")
    loader = DirectoryLoader(data_path, glob="**/*.pdf", loader_cls=UnstructuredFileLoader)
    return loader.load()

