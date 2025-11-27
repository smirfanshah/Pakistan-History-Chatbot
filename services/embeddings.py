from sentence_transformers import SentenceTransformer

embedder = SentenceTransformer("sentence-transformers/all-mpnet-base-v2")

def embed(text: str):
    return embedder.encode(text).tolist()
