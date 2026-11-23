"""Store current-session memory and a local JSON chat history."""
import json
from pathlib import Path

conversation_memory = []
CHAT_HISTORY_FILE = Path(__file__).with_name("chat_history.json")


def load_chat_history():
    """Return recent saved exchanges as text for the assistant prompt."""
    try:
        history = json.loads(CHAT_HISTORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return ""

    if not isinstance(history, list):
        return ""

    recent_items = history[-20:]
    return "\n".join(
        f"Patient: {item.get('question', '')}\nAssistant: {item.get('answer', '')}"
        for item in recent_items
        if isinstance(item, dict)
    )


def save_chat(question, answer):
    """Append an exchange to the local JSON file without exposing it to Git."""
    try:
        history = json.loads(CHAT_HISTORY_FILE.read_text(encoding="utf-8"))
        if not isinstance(history, list):
            history = []
    except (OSError, json.JSONDecodeError):
        history = []

    history.append({"question": question, "answer": answer})
    try:
        CHAT_HISTORY_FILE.write_text(
            json.dumps(history, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError:
        # The app can still answer in-memory if local history cannot be written.
        return
