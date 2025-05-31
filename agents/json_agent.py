from utils.parser_utils import load_json

class JSONAgent:
    def __init__(self, memory):
        self.memory = memory

    def handle(self, filepath):
        data = load_json(filepath)
        required_fields = ["id", "amount", "date"]
        anomalies = [field for field in required_fields if field not in data]

        output = {
            "source": filepath,
            "status": "Processed",
            "anomalies": anomalies,
            "extracted": data
        }

        self.memory.log_event(output)