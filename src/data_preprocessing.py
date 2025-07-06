# #src/data_preprocessing.py

import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from data_ingestion import load_WHO_pdf_documents, load_oncology_pdf_documents

def build_vectorstore(documents, save_path=None):
    print(f"📄 Loaded {len(documents)} documents.")

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(documents)
    print(f"🔪 Split into {len(chunks)} chunks.")

    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    if save_path:
        vectorstore.save_local(save_path)
        print(f"💾 Vectorstore saved to: {save_path}")

    return vectorstore

if __name__ == "__main__":
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vectorstore_dir = os.path.join(base_dir, "vectorstores")
    os.makedirs(vectorstore_dir, exist_ok=True)

    print("🔧 Processing WHO documents (data1)...")
    who_docs = load_WHO_pdf_documents()
    build_vectorstore(who_docs, save_path=os.path.join(vectorstore_dir, "vs_data1"))

    print("\n🔧 Processing Oncology documents (data2)...")
    onco_docs = load_oncology_pdf_documents()
    build_vectorstore(onco_docs, save_path=os.path.join(vectorstore_dir, "vs_data2"))

    print("\n✅ Preprocessing complete.")
