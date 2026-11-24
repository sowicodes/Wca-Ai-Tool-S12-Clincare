import json
import os

# Creating a temporary memory while the app is  running
conversation_memory = []

# File for permanent storage
MEMORY_FILE = "chat_history.json"

# Saving in a temporary memory
def save_chat(question, answer):
    conversation_memory.append({"question": question,"answer": answer})

    history = load_chat_history()
    new_chat={"question":question,"answer": answer}
    
    if new_chat not in history:

# Add a new conversation
        history.append(new_chat)

# Saving back to JSON file

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)
def load_chat_history():
    if not os.path.exists(MEMORY_FILE):
        return []
    
    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    
    except Exception:
        return []

def get_chat_history():
    return load_chat_history()
