## 🧠 Agentic RAG-Powered Medical Assistant

> 🌍 AI-Powered Question Answering System for WHO Guidelines & Oncology Handbooks

---

## 🩺 Problem Statement

Healthcare professionals and medical students often need **quick and reliable access to trusted clinical guidelines**, such as the WHO Essential Medicines list or oncology treatment handbooks. However, manually searching through extensive PDFs or websites is time-consuming and error-prone.

---

## 🚀 Introduction

This project presents an **Agentic RAG (Retrieval-Augmented Generation) Medical Assistant** that uses LLM agents and vector-based semantic search to **answer complex medical queries** by retrieving context from trusted PDF documents.

🧠 It combines:

* **LangChain’s Agent Architecture**
* **FAISS-based vector search**
* **LLMs via Groq’s LLaMA 3.3 70B model**
* **FastAPI Web Interface**
* **Dockerized deployment**
* **CI/CD via GitHub Actions**

---

## 📂 Folder Structure

```
├── data/
│   ├── data1/                 # WHO documents
│   │   └── WHO-MHP-HPS-...pdf
│   └── data2/                 # Oncology handbooks
│       └── medical_oncology_...pdf
├── src/
│   ├── agent.py               # Agent construction logic
│   ├── data_ingestion.py      # Load raw PDFs
│   ├── data_preprocessing.py  # Split & vectorize
│   ├── llm_config.py          # Groq LLM setup
│   ├── tools.py               # Define QA tools
│   └── vectorstore_loader.py  # Load FAISS stores
├── templates/                 # HTML templates (Jinja2)
├── static/                    # Static assets (CSS, JS)
├── tests/                     # Unit tests
├── vectorstores/              # Saved FAISS vector DBs
├── main.py                    # FastAPI app
├── Dockerfile
├── requirements.txt
├── .env                       # API keys
└── .github/
    └── workflows/
        └── ci-cd.yml          # CI/CD config
```

---

## 🛠️ Features

| Feature                   | Description                                                               |
| ------------------------- | ------------------------------------------------------------------------- |
| 📚 PDF RAG Ingestion      | Supports WHO + Oncology documents via `langchain_community` loaders       |
| 🧩 Semantic Vector Search | Uses HuggingFace `all-MiniLM-L6-v2` + FAISS for efficient chunk retrieval |
| 🧠 LLM QA Tools           | Two specialized tools for WHO and Oncology queries                        |
| 🧪 CI Testing             | Pytest integrated for unit testing workflows                              |
| 🐳 Dockerized             | Ready-to-run Docker build with GPU/CPU flexibility                        |
| ⚙️ GitHub Actions CI/CD   | Auto builds, tests, and pushes image to Docker Hub                        |
| 🌐 FastAPI Frontend       | Ask questions via a clean web UI powered by Jinja2                        |

---
# 🏗️ System Architecture
scss
Copy
Edit

            ┌────────────────────────────┐
            │     Medical PDF Corpus     │
            │   (WHO + Oncology docs)    │
            └────────────┬───────────────┘
                         │
        ┌────────────────▼────────────────┐
        │   Data Ingestion & Chunking     │
        │ (Unstructured Loader + Splitter)│
        └────────────────┬────────────────┘
                         │
              ┌──────────▼────────────┐
              │ Vector Embeddings     │
              │ (HuggingFace + FAISS) │
              └──────────┬────────────┘
                         │
        ┌────────────────▼─────────────────┐
        │   LangChain Tools & Agent        │
        │ (Tool1: WHO | Tool2: Oncology)   │
        └────────────────┬─────────────────┘
                         │
              ┌──────────▼────────────┐
              │ Groq-hosted LLaMA3    │
              │ Agent Reasoning Logic │
              └──────────┬────────────┘
                         │
                ┌────────▼────────┐
                │ FastAPI + HTML  │
                │ User Interface  │
                └─────────────────┘


## 🧪 Example Queries

🩺 **WHO Tool:**

> *"What are the essential medicines listed for malaria treatment?"*

🧬 **Oncology Tool:**

> *"What targeted therapies are recommended for non-small cell lung cancer with EGFR mutations?"*

---

## ⚙️ Tech Stack

* 🧠 **LLM**: LLaMA 3.3 70B via [Groq API](https://console.groq.com/)
* 🧰 **LangChain**: RAG, Agent tools, retrievers
* 📦 **FAISS**: Efficient vector search
* 🧬 **Embeddings**: HuggingFace Sentence Transformers
* 🌐 **FastAPI**: Web interface
* 🧪 **Pytest**: Unit testing
* 🐳 **Docker**: Containerization
* 🚀 **GitHub Actions**: CI/CD pipeline

---

## 🔧 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/ka1817/Agentic-RAG-Powered-Medical-Assistant.git
cd Agentic-RAG-Powered-Medical-Assistant
```

### 2. Create `.env` file

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Preprocessing (Vector Store Generation)

```bash
python src/data_preprocessing.py
```

### 5. Start the App

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000](http://localhost:8000)

---

## 🐳 Docker

### Build Image

```bash
docker build -t pranavreddy123/agentic-medical-assistant .
```

### Run Container

```bash
docker run -p 8000:8000 --env-file .env pranavreddy123/agentic-medical-assistant
```

---

## 🔁 CI/CD Pipeline

### GitHub Actions

* ✅ **CI**: On every push/pull request, run tests via `pytest`
* 🚀 **CD**: Build & push Docker image to Docker Hub (`pranavreddy123/agentic-medical-assistant`)

```yaml
📁 .github/workflows/ci-cd.yml
```

---

## 🧪 Testing

```bash
pytest tests/
```

---

## 🌟 Contributing

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/my-feature`)
3. Commit your changes
4. Push to the branch
5. Open a Pull Request 🚀

---

## 👨‍🔬 Future Enhancements

* ✅ Add support for additional medical sources (e.g., UpToDate, NCCN)
* 📈 Implement document summarization for long texts
* 🧪 Integrate semantic evaluation for LLM answers
* 🔍 Streamlit / Gradio interface for chat-like UX
* 📱 Deploy via Hugging Face Spaces or AWS SageMaker

---

## 👨‍💻 Author

**Pranav Reddy**
🔗 GitHub: [@ka1817](https://github.com/ka1817)
🐳 Docker Hub: [pranavreddy123](https://hub.docker.com/u/pranavreddy123)

---

## 📜 License

MIT License © 2025 Pranav Reddy

---

Let me know if you want the same README rendered as an actual Canva design layout (PDF or image)!
