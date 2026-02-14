from pymongo import MongoClient
from langchain.text_splitter import RecursiveCharacterTextSplitter
import pickle

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["market_reports"]
collection = db["reports"]

# Fetch all reports
reports_cursor = collection.find()
texts = []
metadatas = []

for report in reports_cursor:
    texts.append(report["content"])
    metadatas.append({
        "report_id": report["report_id"],
        "title": report["title"],
        "author": report["author"],
        "category": report["category"]
    })

# Split texts into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

all_chunks = []
all_metadatas = []

for i in range(len(texts)):
    chunks = text_splitter.split_text(texts[i])
    all_chunks.extend(chunks)
    all_metadatas.extend([metadatas[i]] * len(chunks))

print(f"Total chunks created: {len(all_chunks)}")

# Save chunks and metadata for embeddings
with open("chunks.pkl", "wb") as f:
    pickle.dump(all_chunks, f)

with open("metadatas.pkl", "wb") as f:
    pickle.dump(all_metadatas, f)
