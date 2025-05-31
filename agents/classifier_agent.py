from utils.parser_utils import detect_format, extract_text_from_pdf, parse_email, load_json
from transformers import pipeline
import json

class ClassifierAgent:
    def __init__(self, memory):
        self.memory = memory
        self.classifier = pipeline("zero-shot-classification", model="MoritzLaurer/DeBERTa-v3-base-mnli-fever-anli")

    def process(self, filepath):
        ftype = detect_format(filepath)

        if ftype == 'PDF':
            content = extract_text_from_pdf(filepath)
        elif ftype == 'Email':
            content = parse_email(filepath)['body']
        elif ftype == 'JSON':
            content = json.dumps(load_json(filepath))
        else:
            content = ""

        # LLM-based intent classification
        candidate_labels = ["Invoice", "RFQ", "Complaint", "Regulation", "Unknown"]
        intent_result = self.classifier(content, candidate_labels)
        intent = intent_result["labels"][0]

        result = {
            "source": filepath,
            "format": ftype,
            "intent": intent
        }

        self.memory.log_event(result)
        return result
