from sentence_transformers import SentenceTransformer
from pinecone import Pinecone, ServerlessSpec
import json
import os
import tqdm
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
INDEX_NAME = "pakistan-history-rag"

def upload_to_pinecone(chunks_path="pakistan_history_chunks.json"):

    pc = Pinecone(api_key=PINECONE_API_KEY)

    if INDEX_NAME not in pc.list_indexes().names():
        pc.create_index(
            name=INDEX_NAME,
            dimension=768,
            metric="cosine",
            spec=ServerlessSpec(
                cloud="aws",
                region="us-east-1"
            )
        )

    index = pc.Index(INDEX_NAME)
    model = SentenceTransformer('sentence-transformers/all-mpnet-base-v2')

    with open(chunks_path, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    batch = []
    for item in tqdm.tqdm(chunks):
        emb = model.encode(item["text"]).tolist()

        batch.append({
            "id": item["id"],
            "values": emb,
            "metadata": {
                "title": item["title"],
                "text": item["text"]
            }
        })

        if len(batch) == 50:     # push in small batches
            index.upsert(batch)
            batch = []

    if batch:
        index.upsert(batch)

    print("Upload completed.")
