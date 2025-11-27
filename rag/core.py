from config.settings import SIMILARITY_THRESHOLD
from services.classification import is_pakistan_history_query
from services.retrieval import retrieve
from services.web_search import tavily_search
from services.generation import generate_text
from rag.prompt_builder import build_prompt

def answer_query(query: str, debug=False):
    # Classification
    if not is_pakistan_history_query(query):
        return {"answer": "This question is not about Pakistan history.", "source": "reject"}

    # Pinecone retrieval
    result = retrieve(query)
    matches = result.get("matches", [])
    top_score = matches[0]["score"] if matches else 0

    if debug:
        print("Top similarity score:", top_score)

    # Low confidence, so do web search
    if top_score < SIMILARITY_THRESHOLD:
        if debug:
            print("\n=== FALLBACK WEB SEARCH ===")

        web_data = tavily_search(query)
        context = "\n".join(item["content"] for item in web_data.get("results", []))

        prompt = build_prompt(query, context)
        answer = generate_text(prompt)
        return {"answer": answer, "source": "web"}

    # High confidence, so using RAG
    context = "\n".join(m["metadata"]["text"] for m in matches[:3])

    if debug:
        print("\n--- RAG CONTEXT ---")
        print(context)

    prompt = build_prompt(query, context)
    answer = generate_text(prompt)
    return {"answer": answer, "source": "rag"}
