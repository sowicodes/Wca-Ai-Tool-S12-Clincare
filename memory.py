
import json
import os

# Temporary memory while the application is running
conversation_memory = []

# File for permanent storage
MEMORY_FILE = "chat_history.json"


# Save a conversation
def save_chat(question, answer):

    new_chat = {
        "question": question,
        "answer": answer
    }

    conversation_memory.append(new_chat)

    history = load_chat_history()

    if new_chat not in history:
        history.append(new_chat)

    # Save conversations to JSON
    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4)


# Load previously saved conversations
def load_chat_history():

    if not os.path.exists(MEMORY_FILE):
        return []

    try:
        with open(MEMORY_FILE, "r", encoding="utf-8") as f:
            history = json.load(f)

            if isinstance(history, list):
                return history

            return []

    except (json.JSONDecodeError, OSError):
        return []


# Get conversation history
def get_chat_history():
    return load_chat_history()


# Clear temporary conversation memory
def clear_chat_history():
    conversation_memory.clear()
