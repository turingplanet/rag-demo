# tests/test_query_router.py
from rag_demo.query_router import classify_question, route_query

def test_classify_question():
    analytical_query = "What is the average stock price for AAPL?"
    general_query = "What are the main products of Apple?"
    
    assert classify_question(analytical_query) == "analytical"
    assert classify_question(general_query) == "general"

def test_route_query():
    analytical_query = "What is the highest stock price?"
    general_query = "Which company has a similar business model to Apple?"
    
    analytical_response = route_query(analytical_query)
    general_response = route_query(general_query)
    
    assert isinstance(analytical_response, str)
    assert isinstance(general_response, str)
    assert len(analytical_response) > 0
    assert len(general_response) > 0

