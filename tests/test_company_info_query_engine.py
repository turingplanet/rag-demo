# tests/test_company_info_query_engine.py
from rag_demo.company_info_query_engine import run_general_query

def test_run_general_query():
    query = "What are the main products of Apple?"
    response = run_general_query(query)
    assert isinstance(response, str)
    assert len(response) > 0
    assert "Apple" in response

