# Clinic FAQ Assistant

A classroom prototype built with Python and Streamlit. It answers common clinic questions from the facts in `faq.py`. Questions that do not match those FAQ categories are sent to Google Gemini with the configured clinic information and the conversation so far. The app keeps the current conversation in Streamlit session memory, avoids repeating an exact question, and can create a session summary when the user ends the chat.

This is an information-only demonstration, not a medical or clinical service. Do not enter real patient names, symptoms, contact details, or medical records. Confirm all sample clinic hours, fees, booking details, and services with the group before presenting them as clinic facts.

## What the app does

- Answers questions about clinic hours, prices, booking, and services using `faq.py`.
- Uses Gemini for other questions, with the FAQ facts and current conversation included as context.
- Refuses common diagnosis and treatment questions and provides an emergency response for some urgent terms. These phrase checks are limited and do not make the app suitable for real clinical use.
- Stores question-and-answer pairs in `chat_history.json`.
- Creates a timestamped JSON file containing the conversation and summary when a session is ended and saved.
- Provides a staff history view that requires an `ADMIN_PASSWORD` setting.

## Project files

```text
app.py             Streamlit interface and chat flow
faq.py             Clinic FAQ facts used by the app
memory.py          Loads and saves chat history and session files
summary.py         Requests a summary from Gemini
requirements.txt   Python packages needed to run the app
.env               Local API key and optional staff password; do not commit
chat_history.json  Saved question-and-answer history
```

## Requirements

- Python 3.10 or newer
- Internet connection for Gemini responses and summaries
- A Google Gemini API key

## Set up on Windows

Open Git Bash or PowerShell in the repository folder. The folder name is `Wca-Ai-Tool-S12-Clincare`.

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it in Git Bash:

```bash
source .venv/Scripts/activate
```

Or activate it in PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install the packages listed for this project:

```bash
python -m pip install -r requirements.txt
```

## Configure the API key

Create a file named `.env` in the repository's top-level folder. Add your own key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```

The app stops at startup if `GEMINI_API_KEY` is missing. Replace the placeholder with your key, but never paste the real key into this README, Python files, GitHub, screenshots, or chat messages. `.env` is listed in `.gitignore` and should remain local.

To enable the **View Saved Session** staff menu, also add a private password to the same local file:

```env
ADMIN_PASSWORD=choose_a_local_staff_password
```

Do not commit or share either value.

## Run the app

With the virtual environment active, from the repository folder run:

```bash
python -m streamlit run app.py
```

Streamlit prints a local address, usually `http://localhost:8501`, and opens the app in a browser. That address works on the computer running Streamlit; it is not a public website link.

Use the sidebar to start a new session, open the staff history view, chat, or end the session and save its summary. In the chat, try questions such as:

- What are the clinic's opening hours?
- What services are offered?
- How much is a consultation?
- How can I book an appointment?

## Group members

- Thomas Osollo Ochieng (2916)
- Soni Mwangi
- Lavinia Nungari
- Peter Kwame

Group name: to be confirmed by the group.

## Privacy and limitations

`chat_history.json` and the timestamped session files contain conversation content. Use synthetic examples only, and check that no private information is included before sharing or committing project files. Gemini questions leave the local computer and are processed by Google's service. The app is an educational prototype and must not be used for diagnosis, treatment, emergencies, or real patient records.
