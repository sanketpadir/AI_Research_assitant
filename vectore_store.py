import pickle
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Load chunks, metadata, and embeddings
with open("chunks.pkl", "rb") as f:
    all_chunks = pickle.load(f)

with open("metadatas.pkl", "rb") as f:
    all_metadatas = pickle.load(f)

# Initialize embeddings object (needed by FAISS)
hf_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Build FAISS vectorstore
vectorstore = FAISS.from_texts(
    texts=all_chunks,
    embedding=hf_embeddings,
    metadatas=all_metadatas,
)

# Save FAISS locally
vectorstore.save_local("faiss_report_db_1")
print("FAISS vectorstore saved successfully!")
