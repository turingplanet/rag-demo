# vector_store_generator.py
from langchain_community.document_loaders import CSVLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from config_utils import load_openai_key

# Load documents from a CSV file
loader = CSVLoader(file_path="./data/company_overview.csv")
documents = loader.load()

# Initialize the OpenAI embeddings model
embeddings_model = OpenAIEmbeddings(openai_api_key=load_openai_key())

# Create a FAISS vector store from the documents
vectorstore = FAISS.from_documents(documents, embeddings_model)

# Serialize the entire vector store to bytes
vectorstore_bytes = vectorstore.serialize_to_bytes()

# Save the serialized vector store to a file
with open('./tmp/faiss_vectorstore.pkl', 'wb') as f:
    f.write(vectorstore_bytes)
