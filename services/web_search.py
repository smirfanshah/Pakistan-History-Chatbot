import requests
from config.settings import TAVILY_API_KEY


def tavily_search(query: str):
    url = "https://api.tavily.com/search"
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "max_results": 5
    }

    response = requests.post(url, json=payload)
    return response.json()
