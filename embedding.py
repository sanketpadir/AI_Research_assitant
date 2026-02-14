import pickle
from langchain_huggingface import HuggingFaceEmbeddings

# Load chunks and metadata
with open("chunks.pkl", "rb") as f:
    texts = pickle.load(f)  # list of strings

with open("metadatas.pkl", "rb") as f:
    metadatas = pickle.load(f)  # list of dicts (if saved as dicts)

# Hugging Face embedding model
hf_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Save embeddings object (not the vectors yet)
with open("embeddings.pkl", "wb") as f:
    pickle.dump(hf_embeddings, f)

print("Embeddings object created and saved successfully!")
