import json
import os
from PyPDF2 import PdfReader

def detect_format(filepath):
    ext = os.path.splitext(filepath)[-1].lower()
    if ext == '.json':
        return 'JSON'
    elif ext == '.pdf':
        return 'PDF'
    elif ext in ['.txt', '.eml']:
        return 'Email'
    return 'Unknown'

def extract_text_from_pdf(filepath):
    reader = PdfReader(filepath)
    return "\n".join(page.extract_text() for page in reader.pages)

def parse_email(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    return {
        "sender": "demo@example.com",
        "subject": content[:40],
        "body": content,
        "urgency": "High" if "urgent" in content.lower() else "Normal"
    }

def load_json(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)