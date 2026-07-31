from langchain_community.vectorstores import FAISS
from src.config import FAISS_PATH
from src.embeddings import get_embedding_model
import streamlit as st
import os


def get_retriever():
    """
    Load the FAISS vector database and return a retriever.
    """

    embedding_model = get_embedding_model()

    # Debug Information
    st.write("### Debug Information")
    st.write("Current Working Directory:", os.getcwd())
    st.write("FAISS Path:", FAISS_PATH)
    st.write("FAISS Folder Exists:", os.path.exists(FAISS_PATH))
    st.write(
        "index.faiss Exists:",
        os.path.exists(os.path.join(FAISS_PATH, "index.faiss"))
    )
    st.write(
        "index.pkl Exists:",
        os.path.exists(os.path.join(FAISS_PATH, "index.pkl"))
    )

    try:
        vector_db = FAISS.load_local(
            FAISS_PATH,
            embedding_model,
            allow_dangerous_deserialization=True,
        )

        st.success("✅ FAISS Vector Database Loaded Successfully")

        return vector_db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": 10,
                "fetch_k": 20,
            },
        )

    except Exception as e:
        st.error("❌ Failed to load FAISS Vector Database")
        st.exception(e)
        raise