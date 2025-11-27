import json
import re
import unicodedata


def clean_text(text):
    text = re.sub(r'\s+', ' ', text)
    text = text.strip()
    return text

def chunk_text(text, max_len=500, overlap=100):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + max_len
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start = end - overlap

    return chunks

def make_ascii_id(text):
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode()
    text = re.sub(r"[^A-Za-z0-9_]+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text.strip("_")


def build_chunks(dataset_path="pakistan_history_dataset.json",
                 output_path="pakistan_history_chunks.json"):

    with open(dataset_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    chunks = []

    for title, text in data.items():
        cleaned = clean_text(text)
        text_chunks = chunk_text(cleaned, max_len=250, overlap=50)

        for idx, c in enumerate(text_chunks):
            safe_id = make_ascii_id(title) + f"_{idx}"
            chunks.append({
                "id": safe_id,
                "title": title,
                "text": c
            })

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(chunks, f, indent=2, ensure_ascii=False)

    print(f"Saved chunks to {output_path} — total: {len(chunks)}")