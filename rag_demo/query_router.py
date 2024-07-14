# query_router.py
from langchain_openai import ChatOpenAI

from company_info_query_engine import run_general_query
from pandas_data_analyzer import run_analytical_query
from config_utils import load_openai_key

llm = ChatOpenAI(model_name="gpt-4o", openai_api_key=load_openai_key())

def classify_question(query):
    confirm_analytical = llm.invoke(f"Does the following question asking anything about cash flow, news sentiment, quarterly earnings, or stock weekly data? Return 'y' if yes, 'n' if no. Question: {query}  y/n:").content.strip().lower()
    if "y" in confirm_analytical.lower():
        return "analytical"

    prompt = f"""Classify the following question as either "analytical" or "general":

    Question: {query}

    An "analytical" question typically involves numerical analysis, statistics, or specific data calculations. It often requires working with structured data like in a pandas DataFrame. Examples include:
    - What is the average stock price for a specific company?
    - Which company has the highest stock price?
    - How has the stock price of a company changed over time?

    A "general" question is broader and relates to company descriptions, products, services, or comparisons that don't require specific data analysis. These questions can typically be answered based on general knowledge about companies. Examples include:
    - What are the main products of Adobe?
    - Which companies compete with Facebook in social media?
    - What is the primary business focus of Google?
    - How does Microsoft's product portfolio compare to Apple's?

    Classification:
    """
    response = llm.invoke(prompt)
    classification = response.content.strip().lower()
    if "analytical" in classification.lower():
        return "analytical"
    else:
        return "general"

def route_query(query):
    question_type = classify_question(query)
    print(f"Question type: {question_type}")
    if question_type == "analytical":
        return run_analytical_query(query)
    else:
        return run_general_query(query)

if __name__ == "__main__":
    query = "What is the average stock price for Apple in 2023, and which month has the highest stock price?"
    query = "What companies focus on beauty and fashion?"
    query = "What is the main difference between Microsoft and Amazon?"
    response = route_query(query)
    print(response)
