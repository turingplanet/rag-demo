# company_info_query_engine.py
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema import StrOutputParser
from config_utils import load_openai_key

# Initialize the embeddings model (required for deserialization)
OPENAI_KEY = load_openai_key()
embeddings_model = OpenAIEmbeddings(openai_api_key=OPENAI_KEY)

# Load the serialized vector store from the file
with open('./tmp/faiss_vectorstore.pkl', 'rb') as f:
    vectorstore_bytes = f.read()

# Deserialize the vector store from bytes
vectorstore = FAISS.deserialize_from_bytes(
    embeddings=embeddings_model, 
    serialized=vectorstore_bytes, 
    allow_dangerous_deserialization=True
)

# Initialize the LLMChain with the prompt and OpenAI model
llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=OPENAI_KEY)

# Define a prompt template for generating an answer
template = """
You are a knowledgeable assistant specializing in company information and market trends. Use the following information to answer the user's question in a natural, conversational manner. Don't mention the source of your information unless specifically asked.

Context: {context}

User's question: {question}

Your conversational Answer:"""
prompt = PromptTemplate.from_template(template)

chain = (
    {"context": RunnablePassthrough(), "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def run_general_query(query):
    # Perform a similarity search
    results = vectorstore.similarity_search(query)
    # Extract the content of the top results
    top_results_content = " ".join([result.page_content for result in results[:3]])
    response = chain.invoke({"question": query, "context": top_results_content})
    return response

if __name__ == "__main__":
    # Perform a similarity search
    query = "What companies have a comparable business model, offering both software products and cloud-based services?"
    response = run_general_query(query)
    print(response)
