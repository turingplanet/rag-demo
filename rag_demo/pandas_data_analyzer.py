# pandas_data_analyzer.py
import pandas as pd
from langchain_experimental.agents import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from config_utils import load_openai_key

# Initialize the OpenAI model
llm = ChatOpenAI(model_name="gpt-4", openai_api_key=load_openai_key())

# Load data into pandas DataFrame
stock_weekly_data_df = pd.read_csv("./data/stock_weekly_data.csv")  
news_sentiment_df = pd.read_csv("./data/news_sentiment.csv")  
quarterly_earnings_df = pd.read_csv("./data/quarterly_earnings.csv")  
cash_flow_df = pd.read_csv("./data/cash_flow.csv")  

# Create the pandas DataFrame agent
agent = create_pandas_dataframe_agent(
    llm, 
    [stock_weekly_data_df, news_sentiment_df, quarterly_earnings_df, cash_flow_df], 
    verbose=True, 
    allow_dangerous_code=True,  
    handle_parsing_errors=True,
    max_iterations=20

)

def run_analytical_query(query):
    response = agent.run(query)
    return response

if __name__ == "__main__":
    query = "What is the average stock price between Nvidia and Apple? Please provide the numbers and the distribution across years."
    response = run_analytical_query(query)
    print(response)
