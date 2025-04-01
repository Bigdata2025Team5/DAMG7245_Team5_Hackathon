from crewai import Agent
import litellm
import os
import base64
import matplotlib.pyplot as plt
from io import BytesIO
from typing import Optional

class CodeAgent(Agent):
    def __init__(self):
        super().__init__(
            name="Code Generator",
            role="Stock Data Analysis Code Creator",
            goal="Generate Python code for analyzing and visualizing stock market data.",
            backstory="An AI agent that creates Python code using Matplotlib and Pandas for financial analysis.",
            llm="gpt-4o",
        )

    def run(self, query, data):
        """Executes the code generation task based on query and stock data."""
        generated_code = self.generate_code(query, data)

        if not generated_code or not generated_code.strip():
            print(" Error: AI-generated code is empty or invalid.")
            return {"generated_code": "No valid code generated.", "chart_path": None}

        chart_base64 = self.execute_generated_code(generated_code)
        
        if chart_base64 is None:
            print("Error: Chart generation failed.")
            return {"generated_code": generated_code, "chart_path": None}

        return {
            "generated_code": generated_code,
            "chart_path": chart_base64
        }

   

    def execute_generated_code(self, code: str) -> Optional[str]:
        """Executes the generated code and returns the base64-encoded chart."""
        try:
            if not code or not code.strip():
                print(" Error: No valid code to execute.")
                return None

            local_vars = {}
            exec(code, {"plt": plt}, local_vars)

            img_buffer = BytesIO()
            plt.savefig(img_buffer, format="png")
            img_buffer.seek(0)

            encoded_image = base64.b64encode(img_buffer.read()).decode("utf-8")
            return f"data:image/png;base64,{encoded_image}"
        
        except Exception as e:
            print(f" Error executing generated code: {str(e)}")
            return None

#  Instantiate the agent
code_agent = CodeAgent()
