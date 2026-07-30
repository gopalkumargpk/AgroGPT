from src.embeddings import get_embedding_model

embedding = get_embedding_model()

vector = embedding.embed_query("What is agriculture?")

print("Embedding Length:", len(vector))
print(vector[:10])