from pinecone import Pinecone
from config.settings import PINECONE_API_KEY, INDEX_NAME
from services.embeddings import embed

pc = Pinecone(api_key=PINECONE_API_KEY)
index = pc.Index(INDEX_NAME)

def retrieve(query: str, top_k: int = 5):
    q_emb = embed(query)
    return index.query(vector=q_emb, top_k=top_k, include_metadata=True)
