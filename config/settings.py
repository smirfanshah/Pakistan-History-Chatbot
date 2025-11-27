import os
from dotenv import load_dotenv

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

INDEX_NAME = "pakistan-history-rag"
MODEL_NAME = "llama-3.1-8b-instant"
SIMILARITY_THRESHOLD = 0.65
