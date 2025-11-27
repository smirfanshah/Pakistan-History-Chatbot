from rag.core import answer_query
from src.data import build_dataset
from src.chunk import build_chunks
from src.pinecone import upload_to_pinecone
import json

if __name__ == "__main__":
    # Uncomment to build dataset and index only once
    
    # with open("data/titles.json") as f:
    #     titles = json.load(f)

    # build_dataset(titles)
    # build_chunks()
    # upload_to_pinecone()

    query = "What role did Pakistan play in the 1952 Colombo Plan energy cooperation project?"
    result = answer_query(query, debug=True)

    print("\nSource:", result["source"])
    print("\nFinal Answer:\n", result["answer"])
