from fpdf import FPDF

def generate_pdf(summary, actions, output_file="meeting_notes.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Add title
    pdf.set_font("Arial", size=16)
    pdf.cell(200, 10, txt="Meeting Notes Summary", ln=True, align="C")

    # Add summary
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Summary:\n{summary}\n")

    # Add action items
    pdf.cell(200, 10, txt="Action Items:", ln=True, align="L")
    for action in actions:
        pdf.multi_cell(0, 10, f"- {action}\n")

    pdf.output(output_file)
    print(f"PDF generated as {output_file}")

# Uncomment to test this function directly
# summary = "Your summarized text here..."
# actions = ["Action item 1", "Action item 2"]
# generate_pdf(summary, actions, "meeting_notes.pdf")
