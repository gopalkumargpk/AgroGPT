import os
import streamlit as st

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 AgroGPT Analytics")

pdf_folder = "data/agriculture"

pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith(".pdf")]

total_documents = len(pdf_files)

total_size = 0
for file in pdf_files:
    total_size += os.path.getsize(os.path.join(pdf_folder, file))

total_size = round(total_size / 1024, 2)

col1, col2, col3 = st.columns(3)

col1.metric("📄 Documents", total_documents)
col2.metric("💾 Total Size", f"{total_size} KB")
col3.metric("🧠 Embedding Model", "MiniLM")

st.divider()

st.subheader("⚙️ AI Configuration")

st.info("""
**LLM:** Gemini Flash

**Embedding Model:** sentence-transformers/all-MiniLM-L6-v2

**Vector Database:** FAISS

**Framework:** LangChain
""")

st.divider()

st.subheader("📁 Uploaded PDFs")

for pdf in pdf_files:
    st.success(pdf)