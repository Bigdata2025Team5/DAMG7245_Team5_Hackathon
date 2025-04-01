from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from datetime import datetime, timedelta
from typing import List
import os
import re
from dotenv import load_dotenv
import requests
import litellm
import matplotlib.pyplot as plt
from backend.core.crew import FinancialCrew  
from backend.agents.web_agent import web_agent
from backend.agents.snowflake_agent import fetch_data 


# Load environment variables
load_dotenv()
 
# FastAPI Initialization
app = FastAPI()
 
# API Keys
openai_api_key = os.getenv("OPENAI_API_KEY")
 
# Request Model
class QueryRequest(BaseModel):
    query: str
 
# Function to detect the company from the query
def detect_company(query: str):
    q = query.lower()
    if "apple" in q:
        return "AAPL_STOCK_HISTORY"
    elif "meta" in q or "facebook" in q:
        return "META_STOCK_HISTORY"
    return None
 
# Function to detect the time period from the query
def detect_duration(query: str) -> datetime:
    q = query.lower()
    patterns = [
        (r'last (\d+) days?', lambda match: datetime.now() - timedelta(days=int(match.group(1)))),
        (r'last (\d+) weeks?', lambda match: datetime.now() - timedelta(weeks=int(match.group(1)))),
        (r'last (\d+) months?', lambda match: datetime.now() - timedelta(days=int(match.group(1)) * 30)),
    ]
 
    for pattern, func in patterns:
        match = re.search(pattern, q)
        if match:
            return func(match)
 
    return datetime.now() - timedelta(days=30)  # Default to last 30 days
 
 
# FastAPI route to handle stock research queries
@app.post("/search")

async def search(request: QueryRequest):

    query = request.query

    sentiment = request.sentiment

    company = detect_company(query)
 
    if not company:

        return JSONResponse(content={"error": "Company not identified in query."}, status_code=400)
 
    start_date = detect_duration(query)

    data = fetch_data(company, start_date)
 
    if not data:

        return JSONResponse(content={"error": "No stock data found for the given period."}, status_code=404)
 
    # Initialize FinancialCrew to generate the report

    financial_crew = FinancialCrew()
 
    # Fetch related news using the web agent

    news = web_agent.fetch_news(company)
 
    # Fetch related stock news via SERP API search

    serp_articles = web_agent.serp_api_search(query, company, sentiment)
 
    # Generate financial report using CrewAI agents, including news and SERP articles

    financial_report, chart_path = financial_crew.generate_financial_report(query, data, news, serp_articles)
 
    return JSONResponse(content={

        "company": company,

        "start_date": start_date.strftime('%Y-%m-%d'),

        "financial_report": financial_report,

        "chart_path": chart_path,  

        "news": news,

        "serp_articles": serp_articles  

    }, status_code=200)
 