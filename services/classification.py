from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def is_pakistan_history_query(query: str) -> bool:
    prompt = f"""
    Determine if the following query is about Pakistan history.
    Respond ONLY: YES or NO.

    Query: "{query}"
    """

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    answer = response.choices[0].message.content.strip().upper()
    return answer == "YES"
