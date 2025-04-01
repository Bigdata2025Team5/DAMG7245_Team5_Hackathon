from crewai import Agent
import snowflake.connector
import os
from datetime import datetime,timedelta
 
class SnowflakeAgent:
    def __init__(self):
        self.agent = Agent(
            name="Snowflake Data Fetcher",
            role="Stock Data Retriever",
            goal="Fetch stock market data from Snowflake database.",
            backstory="An AI agent specialized in retrieving and analyzing stock market data from Snowflake.",
            llm="gpt-4o",
        )
 
    def run(self, task, query, data):
        """Fetches stock data from Snowflake"""
        return self.fetch_data(query)
 
    def fetch_data(self, table: str, start_date: datetime):
        """Fetch stock data based on query"""
        user = os.getenv("SNOWFLAKE_USER")
        password = os.getenv("SNOWFLAKE_PASSWORD")
        account = os.getenv("SNOWFLAKE_ACCOUNT")
        database = os.getenv("SNOWFLAKE_DATABASE")
        schema = os.getenv("SNOWFLAKE_SCHEMA")
 
        # Connect to Snowflake
        conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            database=database,
            schema=schema,
            role="ACCOUNTADMIN"
        )
        cursor = conn.cursor()
 
        cursor.execute("USE ROLE ACCOUNTADMIN;")
        cursor.execute("USE DATABASE ASSIGNMENT;")
        cursor.execute("USE SCHEMA HACKATHON;")
        
        query = f"""
            SELECT * FROM {table}
            WHERE "Date" >= '{start_date.strftime('%Y-%m-%d')}'
            ORDER BY "Date" ASC
        """
 
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]
        rows = cursor.fetchall()
        data = [dict(zip(columns, row)) for row in rows]
 
        cursor.close()
        conn.close()
        return data
 
# Initialize the SnowflakeAgent
snowflake_agent = SnowflakeAgent()
 
 