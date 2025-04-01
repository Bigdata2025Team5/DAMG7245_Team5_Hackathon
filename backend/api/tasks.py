from crewai import Task
from agents.web_agent import web_agent
from agents.snowflake_agent import snowflake_agent
from agents.code_agent import code_agent

from agents.report_agent import report_agent
from agents.risk_agent import risk_agent
from agents.valuation_agent import valuation_agent


# ✅ Company Overview Task
fetch_company_overview = Task(
    name="Company Overview",
    description="Gather details about the company's market presence and business operations.",
    agent=web_agent
)

# ✅ Financial Performance Task
fetch_financial_performance = Task(
    name="Financial Performance",
    description="Extract revenue, earnings, and cash flow trends from Snowflake.",
    agent=snowflake_agent
)

# ✅ Stock Valuation Analysis Task
compute_stock_valuation = Task(
    name="Stock Valuation",
    description="Calculate DCF, P/E, SMA, and other stock price-related metrics.",
    agent=code_agent
)


# ✅ Risk Assessment Task
analyze_risks = Task(
    name="Financial Risk Analysis",
    description="Evaluate company risk factors including market volatility and debt concerns.",
    agent=risk_agent
)

# ✅ Investment Recommendation Task
generate_stock_rating = Task(
    name="Investment Recommendation",
    description="Based on all sections, provide a stock rating (Buy/Hold/Sell).",
    agent=valuation_agent
)

# ✅ Report Generation Task
generate_full_report = Task(
    name="Generate Structured Financial Report",
    description="Compile all sections into a structured, non-repetitive 20-25 page report.",
    agent=report_agent
)
