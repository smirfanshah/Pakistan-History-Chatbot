import wikipediaapi
import json
import time

def fetch_wiki_page(title, wiki):
    for attempt in range(3):  # retry mechanism
        try:
            page = wiki.page(title)
            if page.exists():
                return page.text
            return None
        except Exception as e:
            print(f"[Retry {attempt+1}] Error fetching {title}: {e}")
            time.sleep(2)
    return None


def build_dataset(titles, output_file="pakistan_history_dataset.json"):
    wiki = wikipediaapi.Wikipedia(
        language='en',
        user_agent="PakistanHistoryRAG/1.0"
    )

    dataset = {}
    missing = []

    for idx, title in enumerate(titles):
        print(f"Fetching ({idx+1}/{len(titles)}): {title}")

        text = fetch_wiki_page(title, wiki)

        if text is None:
            print(f"Missing: {title}")
            missing.append(title)
        else:
            print(f"Fetched: {title} ({len(text)} chars)")
            dataset[title] = text

        time.sleep(1.5)  # rate limit control

    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(dataset, f, indent=2, ensure_ascii=False)

    print("\nDataset built successfully!")
    print(f"Saved to: {output_file}")
    print(f"Missing pages: {missing}")

