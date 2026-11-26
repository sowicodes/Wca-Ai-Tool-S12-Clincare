import json
import os
from datetime import datetime

# File that stores questions and answers from all sessions

MEMORY_FILE = "chat_history.json"


def load_chat_history():
    """
    Load saved chat history.
    """

    try:

        # No file or an empty file means there is no history yet
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

    # Handle a file that does not contain valid JSON
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


# Add one pair to the existing history
def save_chat(question, answer):
    """
    Save a single question-answer pair.
    """

    try:

        # Load the old history, add the new pair, then rewrite the file
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


# Save one completed session in its own file
def save_session(conversation, summary):
    """
    Save full session and summary.
    """

    try:

        # The date and time are used in the file name
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

        # Return the name so the app can display it
        return filename

    except Exception as e:

        print(f"Session save error: {e}")

        return None


# Empties the history file (the app does not currently call this)

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