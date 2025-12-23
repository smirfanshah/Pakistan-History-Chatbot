# Pakistan History Question-Answering System

A minimal Retrieval-Augmented Generation (RAG) system that answers questions about Pakistan’s history using semantic search and modern NLP techniques.

## Features

- **Domain Validation**: Filters queries to ensure they are related to Pakistan’s history
- **Retrieval-Augmented Generation**: Combines document retrieval with LLM-based answer generation
- **Vector Search**: Uses Pinecone for semantic similarity search over historical documents
- **Fallback Web Search**: Queries external sources when indexed data is insufficient
- **Confidence-Based Routing**: Selects retrieval or web search based on similarity scores
- **Web Interface**: Simple Gradio-based interface for interactive use

## Architecture

The system implements a multi-stage pipeline:

1. **Query Classification**: Validates if the input is Pakistan history-related
2. **Semantic Retrieval**: Searches Pinecone vector database for relevant documents
3. **Confidence Assessment**: Evaluates retrieval quality using similarity scores
4. **Hybrid Fallback**: Uses Tavily web search for low-confidence results
5. **Answer Generation**: Generates responses using LLaMA 3.1 8B via Groq

### Technology Stack

- **Vector Database**: Pinecone
- **Language Model**: LLaMA 3.1 8B (via Groq)
- **Embeddings**: Sentence Transformers
- **Web Search**: Tavily Search API
- **Data Source**: Wikipedia API
- **Interface**: Gradio

## Prerequisites

- Python 3.8 or higher
- API keys for:
  - [Pinecone](https://pinecone.io/)
  - [Groq](https://groq.com/)
  - [Tavily](https://tavily.com/)


## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/smirfanshah/Pakistan-History-Chatbot.git
   cd Pakistan-History-Chatbot
   ```
2. **Create and activate a virtual environment**
    ```
    python -m venv .venv
    source .venv/bin/activate   # Linux
    ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   PINECONE_API_KEY=your_pinecone_api_key
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

5. **Initialize Pinecone index**

   Index creation is a one-time process. Dataset preparation and vector upload logic is included in main.py.
   ```bash
   python main.py 
   ```

## Usage

### Interactive Web Interface

Launch the Gradio application:
```bash
python app.py
```

The interface will be available at `http://localhost:7860`

### Python API

```python
from rag.core import answer_query

result = answer_query("What role did Pakistan play in the 1952 Colombo Plan?")

print(f"Answer: {result['answer']}")
print(f"Source: {result['source']}")
```

### Command Line

```bash
python main.py
```

This runs a demo query and displays the answer with source attribution.

## Project Structure

```
pakistan-history-qa/
├── app.py                    # Gradio web interface
├── main.py                   # Demo script and initialization
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not in repo)
├── config/
│   └── settings.py          # Configuration settings
├── rag/
│   ├── core.py              # Main RAG pipeline
│   └── prompt_builder.py    # Prompt construction utilities
├── services/
│   ├── classification.py    # Query classification service
│   ├── embeddings.py        # Text embedding utilities
│   ├── generation.py        # LLM text generation
│   ├── retrieval.py         # Pinecone retrieval
│   └── web_search.py        # Tavily web search
├── src/
│   ├── chunk.py             # Text chunking for indexing
│   ├── data.py              # Dataset building utilities
│   └── pinecone.py          # Pinecone upload utilities
└── data_preprocessing/
    ├── pakistan_history_chunks.json
    ├── pakistan_history_dataset.json
    └── titles.json
```

## Configuration

Key settings can be modified in `config/settings.py`:

- `SIMILARITY_THRESHOLD`: Minimum confidence for RAG answers (default: 0.65)
- `MODEL_NAME`: LLM model for generation (default: "llama-3.1-8b-instant")
- `INDEX_NAME`: Pinecone index name (default: "pakistan-history-rag")

## Development

### Building the Knowledge Base

To rebuild the dataset and update the vector index:

1. Modify titles in `data_preprocessing/titles.json`
2. Run the setup:
   ```python
   from src.data import build_dataset
   from src.chunk import build_chunks
   from src.pinecone import upload_to_pinecone
   
   with open("data_preprocessing/titles.json") as f:
       titles = json.load(f)
   
   build_dataset(titles)
   build_chunks()
   upload_to_pinecone()
   ```


## Performance

The system uses a confidence-based approach:
- **High Confidence (>0.65)**: Uses RAG with indexed Pakistan history data
- **Low Confidence**: Falls back to web search for broader information
- **Off-topic Queries**: Automatically rejects non-Pakistan history questions
