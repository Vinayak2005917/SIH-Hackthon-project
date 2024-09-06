# %%
import pandas as pd
import re
import os
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError
import bibtexparser
from django.http import JsonResponse
import csv

def read_from_excel(file_path):
    try:
        excel = pd.read_excel(file_path)
        data_list = excel.values.tolist()  # Convert to list
        csv_file_path = "contents.csv"
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)
        return {"status": "success", "message": f"File saved as {csv_file_path}"}
    except FileNotFoundError:
        return {"status": "error", "message": f"The file does not exist at {file_path}"}
    except Exception as e:
        return {"status": "error", "message": f"An error occurred: {e}"}

def extract_text_from_bibtex(bibtex_file_path):    
    try:
        with open(bibtex_file_path, 'r') as bibfile:
            bib_database = bibtexparser.load(bibfile)
        
        entries = bib_database.entries
        if not entries:
            return {"status": "error", "message": "No entries found in the BibTeX file."}
            
        data_list = [list(entry.values()) for entry in entries]  # Convert to list of lists
        csv_file_path = "contents3.csv"
        with open(csv_file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data_list)
        return {"status": "success", "message": f"Data successfully written to {csv_file_path}"}

    except FileNotFoundError:
        return {"status": "error", "message": f"The file {bibtex_file_path} was not found."}
    except pd.errors.EmptyDataError:
        return {"status": "error", "message": "The CSV file could not be created. DataFrame is empty."}
    except Exception as f:
        return {"status": "error", "message": f"An unexpected error occurred: {f}"}  

def extract_text_from_pdf(pdfpath):
    try:
        with open(pdfpath, 'rb') as file:
            pdf_reader = PdfReader(file)
            text = []
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
        return '\n'.join(text)
    except FileNotFoundError:
        return None
    except PdfReadError:
        return None
    except Exception:
        return None

def text_to_list(text):
    rows = text.split('\n')
    data_list = []
    
    for row in rows:
        columns = re.split(r'\s+', row.strip())
        if len(columns) > 1:
            data_list.append(columns)
    
    return data_list

def pdf_to_csv(pdfpath):
    try:
        text = extract_text_from_pdf(pdfpath)
        if not text:
            raise ValueError("No text extracted from the PDF.")
        data_list = text_to_list(text)
        if data_list:
            csv_file_path = "contents2.csv"
            with open(csv_file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerows(data_list)
            return {"status": "success", "message": f"Data successfully written to {csv_file_path}"}
        else:
            return {"status": "error", "message": "No table data found in the PDF."}
    except ValueError as ve:
        return {"status": "error", "message": str(ve)}
    except Exception as e:
        return {"status": "error", "message": f"An unexpected error occurred: {e}"}

def process_file(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()

    if file_extension == '.xlsx':
        return read_from_excel(file_path)
    elif file_extension == '.bib':
        return extract_text_from_bibtex(file_path)
    elif file_extension == '.pdf':
        return pdf_to_csv(file_path)
    else:
        return {"status": "error", "message": "Unsupported file format."}



