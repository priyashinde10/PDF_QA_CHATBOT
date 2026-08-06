# 📄 PDF AI Assistant using RAG (Retrieval-Augmented Generation)

An AI-powered PDF Question Answering application built using **LangChain**, **FAISS**, **Sentence Transformers**, **Llama 3.2**, **Ollama**, and **Streamlit**.

Users can upload one or more PDF documents, ask questions in natural language, and receive accurate answers generated from the uploaded documents along with the source pages.

---

# 🚀 Features

- 📂 Upload multiple PDF documents
- 📖 Automatic PDF text extraction
- ✂️ Intelligent text chunking
- 🧠 Semantic search using MiniLM embeddings
- 📚 FAISS Vector Database for fast retrieval
- 🤖 AI-generated answers using Llama 3.2 (Ollama)
- 💬 Chat-style conversation interface
- 📑 Source page references
- 📜 Chat history
- 🎨 Modern Streamlit UI

---

# 🛠️ Tech Stack

### Frontend
- Streamlit

### Backend
- Python

### AI & LLM
- LangChain
- Ollama
- Llama 3.2

### Embedding Model
- Sentence Transformers
- all-MiniLM-L6-v2

### Vector Database
- FAISS

### PDF Processing
- PyPDF

---

# 📂 Project Structure

```
PDF_QA_CHATBOT/
│
├── pdfs/
│
├── utils/
│   ├── embeddings.py
│   ├── loader.py
│   ├── splitter.py
│   ├── retriever.py
│   └── qa.py
│
├── vector_db/
│   ├── index.faiss
│   └── index.pkl
│
├── app.py
├── chatbot.py
├── rag.py
├── requirements.txt
├── README.md
└── .env
```

---

# ⚙️ Installation

## 1 Clone Repository

```bash
git clone https://github.com/yourusername/PDF_QA_CHATBOT.git
```

```bash
cd PDF_QA_CHATBOT
```

---

## 2 Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## 3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4 Install Ollama

Download:

https://ollama.com/download

---

## 5 Pull Llama 3.2 Model

```bash
ollama pull llama3.2
```

---

## 6 Run Ollama

```bash
ollama serve
```

---

## 7 Run Streamlit Application

```bash
streamlit run app.py
```

---

# 💡 How It Works

1. Upload one or more PDF documents.
2. Extract text from PDFs.
3. Split documents into chunks.
4. Generate embeddings using MiniLM.
5. Store embeddings in FAISS.
6. Ask a question.
7. Retrieve the most relevant chunks.
8. Pass retrieved context to Llama 3.2.
9. Generate an intelligent answer.
10. Display the answer with source references.

---

# 🧠 AI Models Used

| Component | Model |
|-----------|-------|
| Large Language Model | Llama 3.2 |
| Embedding Model | all-MiniLM-L6-v2 |
| Framework | LangChain |
| Vector Database | FAISS |

---

# 📷 Screenshots

## Home Page

(Add Screenshot Here)

---

## Upload PDFs

(Add Screenshot Here)

---

## Chat Interface

(Add Screenshot Here)

---

## AI Response

(Add Screenshot Here)

---

## Source References

(Add Screenshot Here)

---

# 📈 Future Enhancements

- Voice input
- Speech-to-text
- Text-to-speech
- PDF summarization
- Multi-language support
- Chat export
- Authentication system
- Cloud deployment
- Chat memory across sessions

---

# 👩‍💻 Author

**Priya Shinde**

MCA Student

---

# 📜 License

This project is created for educational and academic purposes.