import json
import os
from datetime import datetime

MEMORY_FILE = "chat_history.json"


def load_chat_history():
    """
    Load saved chat history.
    """

    try:

        if not os.path.exists(MEMORY_FILE):
            return []

        with open(
            MEMORY_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            content = file.read().strip()

            if not content:
                return []

            return json.loads(content)

    except FileNotFoundError:

        print("History file not found.")
        return []

    except json.JSONDecodeError:

        # Keep the damaged file so the next save cannot erase it
        backup = (
            f"{MEMORY_FILE}."
            f"{datetime.now():%Y%m%d%H%M%S%f}.bak"
        )
        os.replace(MEMORY_FILE, backup)
        print(f"Invalid JSON. Moved to {backup}.")
        return []

    except Exception as e:

        print(f"Load error: {e}")
        return []


def save_chat(question, answer):
    """
    Save a single question-answer pair.
    """

    try:

        history = load_chat_history()

        history.append({
            "question": question,
            "answer": answer
        })

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                history,
                file,
                indent=4,
                ensure_ascii=False
            )

    except Exception as e:

        print(f"Save error: {e}")


def save_session(conversation, summary):
    """
    Save full session and summary.
    """

    try:

        filename = (
            f"session_"
            f"{datetime.now():%Y_%m_%d_%H_%M_%S}.json"
        )

        session_data = {
            "conversation": conversation,
            "summary": summary
        }

        with open(
            filename,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                session_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        return filename

    except Exception as e:

        print(f"Session save error: {e}")

        return None


def clear_chat_history():
    """
    Reset chat history file.
    """

    try:

        with open(
            MEMORY_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump([], file)

    except Exception as e:

        print(f"Clear error: {e}")
