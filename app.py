import streamlit as st
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(
    page_title="Market Research RAG Assistant",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Market Research RAG Assistant")
st.markdown("Ask questions about market research reports.")

# ----------------------------
# Load FAISS Vector DB (cached)
# ----------------------------
@st.cache_resource
def load_vectorstore():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(
        "faiss_report_db_1",
        embeddings,
        allow_dangerous_deserialization=True
    )
    return vectorstore

vectorstore = load_vectorstore()

# ----------------------------
# Sidebar Filters
# ----------------------------
st.sidebar.header("🔎 Filters")

category_filter = st.sidebar.selectbox(
    "Select Category",
    ["All", "Automotive", "Chemical and Materials", "Healthcare"]
)

# ----------------------------
# User Query
# ----------------------------
query = st.text_input("💬 Enter your question:")

if st.button("Search") and query:

    with st.spinner("Searching relevant documents..."):

        # Retrieve top 5 results
        docs = vectorstore.similarity_search(query, k=5)

        # Apply category filter manually
        if category_filter != "All":
            docs = [doc for doc in docs if doc.metadata.get("category") == category_filter]

        if len(docs) == 0:
            st.warning("No relevant results found for selected category.")
        else:
            st.success(f"Found {len(docs)} relevant results")

            for i, doc in enumerate(docs):
                with st.expander(f"📄 Result {i+1} - {doc.metadata.get('title')}"):
                    st.write("### 📝 Content Snippet:")
                    st.write(doc.page_content)

                    st.write("### 📌 Metadata:")
                    st.json(doc.metadata)
