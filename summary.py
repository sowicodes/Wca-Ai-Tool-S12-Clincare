"""Build a readable summary from the questions and answers in one session."""
def generate_summary(conversation_memory):
    """Return the session's questions and assistant answers as plain text."""
    if not conversation_memory:
        return "No questions have been asked during this session."
    lines = ["CONVERSATION SUMMARY", ""]
    for number, item in enumerate(conversation_memory, start=1):
        question = item.get("question", "").strip()
        answer = item.get("answer", "").strip()
        lines.extend(
            [
                f"{number}. Patient: {question}",
                "   Assistant:",
                f"   {answer}",
                "-" * 72,
                "",
            ]
        )
    return chr(10).join(lines).rstrip()
