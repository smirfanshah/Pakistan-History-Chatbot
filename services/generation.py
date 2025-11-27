from groq import Groq
from config.settings import GROQ_API_KEY, MODEL_NAME

client = Groq(api_key=GROQ_API_KEY)

def generate_text(prompt: str) -> str:
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    return response.choices[0].message.content
