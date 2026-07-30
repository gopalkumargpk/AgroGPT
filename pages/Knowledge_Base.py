import os
import streamlit as st

st.set_page_config(
    page_title="Knowledge Base",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Knowledge Base")

pdf_folder = "data/agriculture"

if not os.path.exists(pdf_folder):
    st.error("Knowledge Base folder not found.")
    st.stop()

pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

st.metric("Total Documents", len(pdf_files))

st.subheader("Uploaded Documents")

if pdf_files:
    for pdf in pdf_files:
        size = os.path.getsize(os.path.join(pdf_folder, pdf)) / 1024
        st.write(f"✅ **{pdf}** ({size:.1f} KB)")
else:
    st.warning("No PDF documents found.")

st.divider()

st.subheader("Vector Database")

if os.path.exists("database/faiss_index"):
    st.success("✅ FAISS Vector Database is Ready")
else:
    st.error("❌ Vector Database not found")