import os
import streamlit as st

st.set_page_config(
    page_title="Knowledge Base",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Knowledge Base")

# ----------------------------
# PDF Documents
# ----------------------------

pdf_folder = "data/agriculture"

if not os.path.exists(pdf_folder):
    st.error("❌ Knowledge Base folder not found.")
    st.stop()

pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

st.metric("Total Documents", len(pdf_files))

st.subheader("Uploaded Documents")

if pdf_files:
    for pdf in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf)
        size = os.path.getsize(pdf_path) / 1024
        st.write(f"✅ **{pdf}** ({size:.1f} KB)")
else:
    st.warning("No PDF documents found.")

st.divider()

# ----------------------------
# Vector Database
# ----------------------------

st.subheader("Vector Database")

faiss_folder = "database/faiss_index"
faiss_file = os.path.join(faiss_folder, "index.faiss")
pkl_file = os.path.join(faiss_folder, "index.pkl")

if os.path.exists(faiss_file) and os.path.exists(pkl_file):
    st.success("✅ FAISS Vector Database is Ready")

    st.write("**Database Location:**")
    st.code(faiss_folder)

else:
    st.error("❌ Vector Database not found")

    with st.expander("Debug Information"):
        st.write("Current Working Directory:")
        st.code(os.getcwd())

        st.write("Database Folder Exists:")
        st.write(os.path.exists("database"))

        st.write("FAISS Folder Exists:")
        st.write(os.path.exists(faiss_folder))

        st.write("index.faiss Exists:")
        st.write(os.path.exists(faiss_file))

        st.write("index.pkl Exists:")
        st.write(os.path.exists(pkl_file))