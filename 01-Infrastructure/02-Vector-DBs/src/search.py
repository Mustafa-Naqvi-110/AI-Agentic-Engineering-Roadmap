import chromadb
from sentence_transformers import SentenceTransformer

# 1. Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Connect to Persistent Storage (crucial so data isn't lost)
client = chromadb.PersistentClient(path="./chroma_db")

# 3. Get the collection (ensure the name matches what you used in ingest.py)
collection = client.get_or_create_collection(name="notes")

while True:
    query = input("\nAsk something (or type 'exit'): ")
    if query.lower() == "exit":
        break

    # Convert query to embedding
    query_embedding = model.encode(query).tolist()

    # Search
    results = collection.query(
    query_embeddings=[query_embedding],
    n_results=1  # Only get the top 1 result
    )

    print("\nRelevant Notes:\n")
    # Check if results exist to avoid indexing errors
    if results["documents"] and len(results["documents"][0]) > 0:
        for doc in results["documents"][0]:
            print("-" * 40)
            print(doc)
    else:
        print("No matching notes found.")