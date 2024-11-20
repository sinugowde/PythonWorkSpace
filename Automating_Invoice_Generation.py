from fpdf import FPDF

def create_invoice(client_name, amount):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Invoice", ln=True, align='C')
    pdf.cell(200, 10, txt=f"Client: {client_name}", ln=True, align='L')
    pdf.cell(200, 10, txt=f"Amount: ${amount}", ln=True, align='L')
    pdf.output(f"{client_name}_invoice.pdf")
    print(f"Invoice for {client_name} created successfully!")

create_invoice('John Doe', 500)