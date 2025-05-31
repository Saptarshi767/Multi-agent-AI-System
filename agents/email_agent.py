from utils.parser_utils import parse_email

class EmailAgent:
    def __init__(self, memory):
        self.memory = memory

    def handle(self, filepath):
        data = parse_email(filepath)
        output = {
            "source": filepath,
            "sender": data["sender"],
            "urgency": data["urgency"],
            "intent": "RFQ",
            "status": "Processed"
        }

        self.memory.log_event(output)