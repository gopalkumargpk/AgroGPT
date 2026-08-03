import os
from langchain_community.vectorstores import FAISS

from src.config import FAISS_PATH
from src.embeddings import get_embedding_model
from src.vector_store import create_vector_store


def get_retriever():

    # Agar FAISS database nahi hai to automatically create karo
    if (
        not os.path.exists(FAISS_PATH)
        or not os.path.exists(os.path.join(FAISS_PATH, "index.faiss"))
        or not os.path.exists(os.path.join(FAISS_PATH, "index.pkl"))
    ):
        create_vector_store()

    embedding_model = get_embedding_model()

    vector_db = FAISS.load_local(
        FAISS_PATH,
        embedding_model,
        allow_dangerous_deserialization=True,
    )

    return vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 10,
            "fetch_k": 20,
        },
    )