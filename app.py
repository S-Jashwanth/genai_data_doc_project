
from flask import Flask, request, render_template, send_file
import os
from utils.doc_generator import generate_metadata_summary
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
PDF_FOLDER = "pdfs"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PDF_FOLDER, exist_ok=True)

def create_pdf(documentation, filename):
    file_path = os.path.join(PDF_FOLDER, filename)
    c = canvas.Canvas(file_path, pagesize=letter)
    width, height = letter
    lines = documentation.split('\n')
    y = height - 50
    for line in lines:
        if y < 50:
            c.showPage()
            y = height - 50
        c.drawString(50, y, line)
        y -= 15
    c.save()
    return file_path

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/upload", methods=["POST"])
def upload_file():
    if "dataset" not in request.files:
        return "No file part"
    file = request.files["dataset"]
    if file.filename == "":
        return "No selected file"
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)
    
    documentation = generate_metadata_summary(file_path)
    
    pdf_filename = file.filename.replace(".csv", "_documentation.pdf")
    pdf_path = create_pdf(documentation, pdf_filename)
    
    return render_template("index.html", documentation=documentation, pdf_file=pdf_filename)

@app.route("/download/<pdf_file>", methods=["GET"])
def download_pdf(pdf_file):
    pdf_path = os.path.join(PDF_FOLDER, pdf_file)
    return send_file(pdf_path, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
