# tests/test_pandas_data_analyzer.py
from rag_demo.pandas_data_analyzer import run_analytical_query

def test_run_analytical_query():
    query = "What is the average stock price for AAPL?"
    response = run_analytical_query(query)
    assert isinstance(response, str)
    assert len(response) > 0
    assert "AAPL" in response
