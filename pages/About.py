import streamlit as st

st.set_page_config(
    page_title="About",
    page_icon="ℹ️",
    layout="wide"
)

st.title("ℹ️ About AgroGPT")

st.markdown("""
## 🌾 AgroGPT

AgroGPT is an AI-powered Agriculture Question Answering System.

It uses Retrieval-Augmented Generation (RAG) to answer questions from uploaded PDF documents.

---

## 🚀 Technologies Used

- Streamlit
- LangChain
- Google Gemini
- HuggingFace Embeddings
- FAISS Vector Database
- Python

---

## ✨ Features

- 📄 Upload Agriculture PDFs
- 📚 Build Knowledge Base
- 🤖 AI Chat
- 🔍 Semantic Search
- ⚡ Fast Retrieval
- 🧠 RAG Pipeline

---

## 👨‍💻 Developed By

Gopal Kumar
M.Tech (AI & ML)
SR University
""")