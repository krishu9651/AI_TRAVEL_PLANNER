from fpdf import FPDF
import os

def generate_pdf(content, filename="output/travel_plan.pdf"):
    os.makedirs("output", exist_ok=True)

    clean_content = content.replace("₹", "Rs.").replace("–", "-").replace("’", "'")

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in clean_content.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output(filename)
    return filename