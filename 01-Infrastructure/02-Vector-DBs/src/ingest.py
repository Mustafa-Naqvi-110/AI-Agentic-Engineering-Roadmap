import os
import chromadb
from sentence_transformers import SentenceTransformer

# 1. Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# 2. Initialize Chroma Persistent Client 
# This ensures data is saved to disk in a folder called 'chroma_db'
client = chromadb.PersistentClient(path="./chroma_db")

# 3. Create or get collection
collection = client.get_or_create_collection(name="notes")

# 4. Corrected Path (Relative to your root 'Python Learning' folder)
notes_dir = "search_your_notes_chromadb/notes"

documents = []
ids = []

# Check if the directory exists to prevent the FileNotFoundError
if not os.path.exists(notes_dir):
    print(f"Error: The directory '{notes_dir}' was not found.")
else:
    # 5. Read notes from the directory
    for idx, filename in enumerate(os.listdir(notes_dir)):
        file_path = os.path.join(notes_dir, filename)
        
        # Only read files (skips folders if any exist in 'notes')
        if os.path.isfile(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                documents.append(f.read())
                ids.append(str(idx))

    if documents:
        # 6. Generate Embeddings
        embeddings = model.encode(documents).tolist()

        # 7. Store in ChromaDB
        collection.add(
            embeddings=embeddings,
            documents=documents,
            ids=ids
        )
        print(f"Success: {len(documents)} notes stored in ChromaDB at ./chroma_db")
    else:
        print("No documents found to index.")