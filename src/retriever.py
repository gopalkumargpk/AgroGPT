from langchain_community.vectorstores import FAISS

from src.config import FAISS_PATH
from src.embeddings import get_embedding_model


def get_retriever():
    """
    Load the FAISS vector database and return a retriever.
    """

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