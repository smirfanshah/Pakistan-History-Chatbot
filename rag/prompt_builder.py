def build_prompt(query, context):
    return f"""
You are a Pakistan history expert. Answer using the provided context.

Context:
{context}

Question:
{query}

Answer in detail and cite events when needed.
    """
