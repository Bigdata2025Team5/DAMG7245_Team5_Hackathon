# Apple & Meta Stock Market Report Generation System

## Project Summary

This project is a full automation of a **financial report generation system** that visualizes and analyzes stock market data for **Apple** and **Meta** based on natural language user queries. 

Essentially, the system incorporates **historical stock data**, **real-time news**, **web content**, and the features of **OpenAI's language models** to give a comprehensive and dynamic stock research report.

---

###  How it Works:

1. **User Query**  
   The user submits a query through a **Streamlit** interface (e.g: "Show Apple stock performance from March 1 to March 15")

2. **Query Understanding (FastAPI Backend)**  
   The backend uses FastAPI to:
   - Detect which company the user is asking about (Apple or Meta)
   - Parse the date range or relative time (e.g: "last month")
   - CrewAI triggers the necessary actions in response to the query: retrieving historical stock data, fetching real-time news, and web results

3. **Code Generation**  
   The system sends the user query and stock data sample to **OpenAI**, which generates Python code (using `matplotlib` and `pandas`) to create visualizations based on the data

4. **Dynamic Code Execution**  
   The generated code is **executed in real time using Python's built-in `exec()` function**, and the resulting chart is saved and returned to the user as an image

5. **Research Report Generation**  
   CrewAI assembles all the findings into a structured research report. Various agents collaborate to create a comprehensive report:
   - `Snowflake Agent`: Analyzes stock data trends and price movements
   - `Web Agent`: Summarizes results from web searches and retrieves relevant content
   - `News Agent`: Interprets the latest headlines and sentiment about the company
   - `Code Agent`: Generates the charts and visualizations.
   - `Valuation Agent`: Offers insights into the stock's valuation and performance
   - `Risk Agent`: Identifies potential risks based on the analysis of data, sentiment, and web content

7. **Final Output**  
   The user sees multi-section research report

---

## Technologies Used

- **FastAPI** – Backend API to handle query routing and agent orchestration
- **Streamlit** – Frontend interface for user interaction and results display
- **Snowflake** – Data warehouse for storing historical stock data
- **OpenAI (via LiteLLM)** – For code generation and report creation
- **SERP API** – For live web search results
- **NewsAPI** – For real-time news headlines
- **CrewAI** – Multi-agent framework to structure financial report logic
- **Python (`exec()`)** – To dynamically execute generated matplotlib code
- **matplotlib & pandas** – Used inside generated code for data visualization

---

## Architecture Diagram

![Apple & Meta Stock Market Report Generation System](https://github.com/Bigdata2025Team5/DAMG7245_Team5_Hackathon/blob/133320e1ef302905800c8d9a2d1b53f309175bf3/Architecture_diagram.png)
