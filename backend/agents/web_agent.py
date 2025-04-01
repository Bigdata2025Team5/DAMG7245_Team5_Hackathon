from crewai import Agent
import requests
import os
 
class WebAgent:
    def __init__(self):
        self.agent = Agent(
            name="Web Research Agent",
            role="Financial News Fetcher",
            goal="Fetches company-related news and market trends.",
            backstory="An AI agent specialized in gathering financial news from the web to help traders make informed decisions.",
            llm="gpt-4o",
        )
        self.serp_api_key = os.getenv("WEB_SEARCH_API_KEY")  # Load SerpAPI key from environment
 
    def run(self, task, query, data):
        """Processes financial news search task"""
        return self.fetch_news(query)  
 
    def fetch_news(self, company_name):
        try:
            api_key = os.getenv("NEWS_API_KEY")  
            url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey={api_key}"
            response = requests.get(url)
            news_data = response.json()
 
            if "articles" in news_data:
                return news_data["articles"][:5]
            else:
                return "No news available."
        except Exception as e:
            return f"Failed to fetch news. Error: {str(e)}"
 
    def serp_api_search(self, query: str, company: str, sentiment: str):
        if sentiment != "finance":
            return {"error": "Sentiment must be 'finance' for stock-related queries."}
        
        url = "https://serpapi.com/search"
        params = {
            'q': f"{company} stock",  
            'api_key': self.serp_api_key,
            'engine': 'google',
        }
 
        response = requests.get(url, params=params)
 
        print("SERP API Response:", response.text)  
 
        if response.status_code == 200:
            data = response.json()
            print("Parsed SERP API Data:", data)  
            
            if "organic_results" not in data:
                return {"error": "No organic_results found in API response"}
 
            articles = []
            for i, result in enumerate(data["organic_results"][:5]):  # Top 5 results
                if isinstance(result, dict):
                    article = {
                        'title': result.get("title", "No Title"),
                        'link': result.get("link", "#"),
                        'snippet': result.get("snippet", ""),
                        'source': result.get("source", "Unknown"),
                    }
                    articles.append(article)
                    if i >= 4:  
                        break
            
            return articles
        else:
            return {"error": f"Failed to fetch data from SERP API. Status code: {response.status_code}"}
 
 
# Initialize the WebAgent
web_agent = WebAgent()
 