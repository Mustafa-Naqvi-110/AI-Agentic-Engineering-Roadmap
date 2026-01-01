# 🔍 Module 02: Vector Databases & Semantic Search

![Status](https://img.shields.io/badge/Status-Completed-success)
![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Focus](https://img.shields.io/badge/Focus-RAG%20%26%20Embeddings-orange)

This module introduces the core engine of **RAG (Retrieval Augmented Generation)**. It moves beyond simple keyword search to **Semantic Search**, enabling AI agents to understand the *meaning* behind a user's query and retrieve relevant context from a private knowledge base.

---

## 🧠 Module Goal
**To give AI Agents "Long-Term Memory".**
LLMs have limited context windows. To build agents that know about your specific data (notes, docs, code), we must learn to **Embed** text into vectors, store them in a **Vector Database** (ChromaDB), and retrieve them based on conceptual similarity.

## 📂 Repository Structure

```text
02-Vector-DBs/
├── notes/               # Knowledge Base (Text files)
│   ├── meeting_notes.txt
│   └── project_ideas.txt
├── src/                 # Source Code
│   ├── ingest.py        # ETL Pipeline: Load -> Embed -> Store
│   └── search.py        # Query Interface: Ask -> Retrieve
└── chroma_db/           # Generated Persistent Database (Auto-created)
```

## 🛠️ Key Concepts Implemented

* **Embeddings:** Using `SentenceTransformer` (`all-MiniLM-L6-v2`) to convert human-readable text into mathematical vectors (lists of numbers).
* **Persistent Storage:** Setting up `chromadb.PersistentClient` so data survives after the script stops running.
* **Ingestion Pipeline:** A script (`ingest.py`) that scans a directory, reads files, and populates the database.
* **Semantic Querying:** A search interface (`search.py`) that finds the most relevant notes even if the exact keywords don't match (e.g., searching "plans" finds "strategy").

---

## 💻 How to Run

**Prerequisites:**
1. Navigate to this folder: `cd 02-Vector-DBs`
2. Install Dependencies:
   ```bash
   pip install chromadb sentence-transformers
   ```
3. Important: Ensure you have text files inside the `notes/` folder.

### 1. Ingest Data (Build the Brain)
*Reads text files from `notes/`, creates embeddings, and saves them to `chroma_db`.*
```bash
python src/ingest.py
```

### 2. Search Data (Test the Memory)
*Launch an interactive loop to ask questions against your notes.*
```bash
python src/search.py
