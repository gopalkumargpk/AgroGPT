from langchain_community.document_loaders import PyPDFDirectoryLoader
from src.config import DATA_PATH


def load_documents():
    """
    Load all PDF files from the data/agriculture folder.
    """

    loader = PyPDFDirectoryLoader(DATA_PATH)
    documents = loader.load()

    print(f"✅ Loaded {len(documents)} pages.")

    return documents