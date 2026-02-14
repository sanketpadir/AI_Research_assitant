from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# Initialize embeddings
hf_embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# Load FAISS vectorstore (FIX HERE)
vectorstore = FAISS.load_local(
    "faiss_report_db_1",
    hf_embeddings,
    allow_dangerous_deserialization=True
)

# Query example
query = "What is the future outlook of the automotive mirror market?"

docs = vectorstore.similarity_search(query, k=3)

for i, doc in enumerate(docs):
    print(f"\n--- Result {i+1} ---")
    print(doc.page_content)
    print(doc.metadata)
