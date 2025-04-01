from fpdf import FPDF

def save_report_as_pdf(report_text, filename="financial_report.pdf"):
    """Saves AI-generated report as a formatted PDF"""
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in report_text.split("\n"):
        pdf.cell(200, 10, txt=line, ln=True)

    pdf.output(filename)
    print(f"✅ Report saved as {filename}")

def save_report_as_markdown(report_text, filename="financial_report.md"):
    """Saves AI-generated report as a Markdown file"""
    with open(filename, "w", encoding="utf-8") as file:
        file.write(report_text)
    print(f"✅ Report saved as {filename}")

def save_report_as_html(report_text, filename="financial_report.html"):
    """Saves AI-generated report as an HTML file"""
    html_content = f"<html><body><pre>{report_text}</pre></body></html>"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"✅ Report saved as {filename}")

# Example Usage:
report_text = "Generated Financial Report..."  # Get AI output
save_report_as_pdf(report_text)
save_report_as_markdown(report_text)
save_report_as_html(report_text)
