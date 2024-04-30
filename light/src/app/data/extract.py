from PyPDF2 import PdfReader
import os

# Get the directory of the current script
script_dir = os.path.dirname(__file__)

# Construct the path to the PDF file relative to the script directory
pdf_path = os.path.join(script_dir, "original_pdf", "part1.pdf")
output_dir = os.path.join(script_dir, "text_file")

# Extract text from pdf and save it in a directory  
def extract_text_from_pdf(pdf_path, output_dir):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    # save in a directory 
    output_path = os.path.join(output_dir, os.path.basename(pdf_path).replace('.pdf', '.txt'))
    with open(output_path, "w") as f:
        f.write(text)
    return text

pdf_path = os.path.join(script_dir, "original_pdf", "part4.pdf")
output_dir = os.path.join(script_dir, "text_file")
extracted_text = extract_text_from_pdf(pdf_path, output_dir)
print(extracted_text)
