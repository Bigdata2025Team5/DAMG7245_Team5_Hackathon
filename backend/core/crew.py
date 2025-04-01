# financial_crew.py

from backend.api.tasks import fetch_company_overview, fetch_financial_performance, generate_full_report

from report_generator import save_report_as_pdf, save_report_as_markdown, save_report_as_html

from agents.web_agent import web_agent

from agents.snowflake_agent import snowflake_agent

from agents.code_agent import code_agent

from agents.report_agent import report_agent

from agents.risk_agent import risk_agent

from agents.valuation_agent import valuation_agent
 
class FinancialCrew:

    def __init__(self):

        self.agents = {

            "report": report_agent,

            "risk": risk_agent,

            "valuation": valuation_agent,

            "web": web_agent,

            "snowflake": snowflake_agent,

            "code": code_agent,

        }

        self.tasks = [fetch_company_overview, fetch_financial_performance, generate_full_report]  # Add tasks here
 
    def generate_financial_report(self, query, data, news, serp_articles):

        """Runs multiple agents to generate a structured financial report, now with news and serp_articles."""

        report_sections = []

        chart_path = None  
 
        # Execute tasks (fetch company overview, financial performance, etc.)

        for task in self.tasks:

            # Here you can run each task, e.g., task.agent.run() with task-specific data

            section = task.agent.run(task=task.description, query=query, data=data)

            report_sections.append(section)

        # Add the agent-based analysis (web, snowflake, etc.)

        for key, agent in self.agents.items():

            task_description = f"Executing {key} analysis for {query}"

            section = agent.run(task=task_description, query=query, data=data)

            report_sections.append(section)
 
        # Generate a structured financial report

        report_text = "\n\n".join(report_sections)
 
        # Save the report in different formats

        save_report_as_pdf(report_text, "financial_report.pdf")

        save_report_as_markdown(report_text, "financial_report.md")

        save_report_as_html(report_text, "financial_report.html")
 
        return report_text, chart_path

 