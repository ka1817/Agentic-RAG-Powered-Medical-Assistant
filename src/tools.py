# src/tool_factory.py

from langchain.chains import RetrievalQA
from langchain.agents import Tool

def build_tool(name: str, description: str, vectorstore, llm):
    retriever = vectorstore.as_retriever(search_kwargs={"k": 3})
    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)

    return Tool(
        name=name,
        func=qa.run,
        description=description
    )
