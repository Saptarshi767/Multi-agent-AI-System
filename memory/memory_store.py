import json
import os

class MemoryStore:
    def __init__(self):
        self.memory = {}
        self.log_path = "outputs/logs.json"
        os.makedirs("outputs", exist_ok=True)

    def save_context(self, key, value):
        self.memory[key] = json.dumps(value)

    def get_context(self, key):
        value = self.memory.get(key)
        return json.loads(value) if value else None

    def log_event(self, event_data):
        log_key = f"log:{event_data['source']}"
        self.save_context(log_key, event_data)

        # Save to outputs/logs.json
        all_logs = []
        if os.path.exists(self.log_path):
            with open(self.log_path, "r") as f:
                try:
                    all_logs = json.load(f)
                except json.JSONDecodeError:
                    all_logs = []

        all_logs.append(event_data)

        with open(self.log_path, "w") as f:
            json.dump(all_logs, f, indent=2)
