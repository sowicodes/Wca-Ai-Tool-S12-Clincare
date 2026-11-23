"""Keep session memory and a small local JSON history for the clinic assistant."""
import json
from pathlib import Path

conversation_memory = []
CHAT_HISTORY_FILE = Path(__file__).with_name("chat_history.json")
MAX_SAVED_EXCHANGES = 20


def _read_history():
    """Load saved exchanges; return an empty list if the file is missing or invalid."""
    try:
        history = json.loads(CHAT_HISTORY_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return []

    return history if isinstance(history, list) else []


def load_chat_history():
    """Format the most recent saved exchanges for the Gemini prompt."""
    lines = []
    for item in _read_history()[-MAX_SAVED_EXCHANGES:]:
        if not isinstance(item, dict):
            continue

        question = item.get("question", "")
        answer = item.get("answer", "")
        if not isinstance(question, str) or not isinstance(answer, str):
            continue

        lines.append(f"Patient: {question}\nAssistant: {answer}")

    return "\n".join(lines)


def save_chat(question, answer):
    """Save an exchange locally, retaining only the latest 20 entries."""
    if not isinstance(question, str) or not isinstance(answer, str):
        return False

    history = _read_history()
    history.append({"question": question, "answer": answer})
    history = history[-MAX_SAVED_EXCHANGES:]

    try:
        CHAT_HISTORY_FILE.write_text(
            json.dumps(history, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    except OSError:
        # The assistant can still reply even if local history cannot be saved.
        return False

    return True
