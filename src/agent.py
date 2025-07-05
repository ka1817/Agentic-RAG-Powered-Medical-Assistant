# src/agent.py

import os
import warnings
warnings.filterwarnings('ignore')
from langchain.agents import initialize_agent, AgentType
from vectorstore_loader import load_vectorstore
from tools import build_tool
from llm_config import load_llm
from data_ingestion import load_WHO_pdf_documents, load_oncology_pdf_documents
from data_preprocessing import build_vectorstore

def ensure_vectorstores_exist():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    vectorstore_dir = os.path.join(base_dir, "vectorstores")
    vs1_path = os.path.join(vectorstore_dir, "vs_data1", "index.faiss")
    vs2_path = os.path.join(vectorstore_dir, "vs_data2", "index.faiss")

    os.makedirs(vectorstore_dir, exist_ok=True)

    if not os.path.exists(vs1_path):
        print("🔧 Vectorstore for WHO not found. Creating...")
        who_docs = load_WHO_pdf_documents()
        build_vectorstore(who_docs, save_path=os.path.join(vectorstore_dir, "vs_data1"))

    if not os.path.exists(vs2_path):
        print("🔧 Vectorstore for Oncology not found. Creating...")
        onco_docs = load_oncology_pdf_documents()
        build_vectorstore(onco_docs, save_path=os.path.join(vectorstore_dir, "vs_data2"))

def get_agent():
    """Initializes and returns the Agentic RAG agent."""
    ensure_vectorstores_exist()
    llm = load_llm()

    vs_who = load_vectorstore("vs_data1")
    vs_onco = load_vectorstore("vs_data2")

    tools = [
        build_tool(
            name="WHO_Medicine_Tool",
            description="Use this tool to answer questions about WHO's essential medicines list.",
            vectorstore=vs_who,
            llm=llm
        ),
        build_tool(
            name="Oncology_Treatment_Tool",
            description="Use this tool for cancer treatment, chemotherapy, oncology emergencies, etc.",
            vectorstore=vs_onco,
            llm=llm
        )
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=False
    )

    return agent

if __name__ == "__main__":
    agent = get_agent()
    response = agent.invoke("What targeted therapies are recommended for non-small cell lung cancer with EGFR mutations?")
    print(f"\n🧠 Agent Response:\n{response['output'].strip()}")
