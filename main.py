from agents.classifier_agent import ClassifierAgent
from agents.json_agent import JSONAgent
from agents.email_agent import EmailAgent
from memory.memory_store import MemoryStore

def main():
    filepath = input("Enter path to input file: ").strip()

    memory = MemoryStore()
    classifier = ClassifierAgent(memory)
    json_agent = JSONAgent(memory)
    email_agent = EmailAgent(memory)

    result = classifier.process(filepath)

    print(f"\n📦 Detected Format: {result['format']}")
    print(f"🎯 Detected Intent: {result['intent']}\n")

    if result["format"] == "Email":
        email_agent.handle(filepath)
        print("✅ Routed to EmailAgent and processed.")
    elif result["format"] == "JSON":
        json_agent.handle(filepath)
        print("✅ Routed to JSONAgent and processed.")
    else:
        print("❌ No matching agent found for this format.")

    print("\n🧠 Memory Log:")
    log = memory.get_context(f"log:{filepath}")
    print(log)

if __name__ == "__main__":
    main()
