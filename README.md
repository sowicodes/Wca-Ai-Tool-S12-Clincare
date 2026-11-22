# Wca-Ai-Tool-S12-Clincare
# 🏥 Clinic FAQ Assistant

An AI-powered chatbot built with **Python, Streamlit, and Google Gemini** that helps patients access clinic information quickly and efficiently. The assistant answers frequently asked questions about clinic services, opening hours, consultation fees, and appointment booking while maintaining conversation memory, refusing diagnosis requests, and generating a session summary.

---

##  Project Overview

The Clinic FAQ Assistant is designed to automate responses to common patient inquiries in a healthcare setting. By combining a structured FAQ knowledge base with Google's Gemini AI model, the system provides both accurate and conversational responses.

The chatbot can:

- Answer questions about clinic services
- Provide opening hours
- Explain consultation costs
- Guide patients on appointment booking
- Remember previously asked questions
- Refuse diagnosis-related requests
- Generate a session summary at the end of the conversation

---

##  Objectives

The main objectives of this project are:

1. Provide instant access to clinic information.
2. Reduce repetitive inquiries handled by clinic staff.
3. Demonstrate the integration of Generative AI in healthcare support.
4. Implement conversation memory.
5. Prevent unsafe diagnosis generation.
6. Generate a summary of user interactions.

---

## Features

### ✅ FAQ-Based Responses

The chatbot responds to frequently asked questions regarding:

- Opening hours
- Services offered
- Consultation fees
- Appointment booking

### ✅ Google Gemini AI Integration

Questions that do not directly match predefined FAQ entries are processed using **Google Gemini AI**, enabling natural language understanding and intelligent responses.

### ✅ Conversation Memory

The chatbot remembers questions already asked during the current session and avoids repeating answers.

### ✅ Diagnosis Refusal

The chatbot refuses requests for medical diagnoses or treatment recommendations.

Example:

**User**

```text
What disease do I have?
```

**Bot**

```text
I cannot provide a diagnosis or medical advice.

Please consult a qualified healthcare professional.
```

### ✅ Session Summary

At the end of the session, users can type:

```text
exit
```

to receive a complete summary of all questions and answers.

---

## 🏗️ System Architecture

```text
                 +------------------+
                 |      User        |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 |   Streamlit UI   |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Question Handler |
                 +--------+---------+
                          |
           +--------------+--------------+
           |                             |
           v                             v
 +------------------+        +----------------------+
 | FAQ Knowledge    |        | Google Gemini AI     |
 | Base             |        | Natural Language     |
 +--------+---------+        +----------+-----------+
          |                             |
          +--------------+--------------+
                         |
                         v
                 +------------------+
                 |  Response Engine |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Memory & Storage |
                 +--------+---------+
                          |
                          v
                 +------------------+
                 | Session Summary  |
                 +------------------+
```

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend Development |
| Streamlit | Web User Interface |
| Google Gemini AI | Natural Language Processing |
| JSON | Chat History Storage |
| python-dotenv | Environment Variable Management |
| Git & GitHub | Version Control |

---

## 📁 Project Structure

```text
Wca-Ai-Tool-S12-Clincare/
│
├── app.py
├── faq.py
├── memory.py
├── summary.py
├── chat_history.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 📄 Project Files

### app.py

Main application file responsible for:

- User interface
- Gemini integration
- FAQ processing
- Memory handling
- Session summary generation

### faq.py

Stores clinic FAQ information.

Example:

```python
faq_data = {
    "hours": "...",
    "prices": "...",
    "booking": "...",
    "services": "..."
}
```

### memory.py

Manages:

- Temporary conversation memory
- Permanent JSON storage
- Chat history retrieval

### summary.py

Generates a structured summary of questions and answers.

### chat_history.json

Stores previous interactions in JSON format.

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/sowicodes/Wca-Ai-Tool-S12-Clincare.git
```

### 2. Navigate to the Project Folder

```bash
cd Wca-Ai-Tools-S12-Clincare
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install google-genai python-dontenv or python -m pip install google-genai python dotenv

pip install streamlit
```

---

## 📦 requirements.txt

```text
streamlit>=1.40.0
google-genai>=1.0.0
python-dotenv>=1.0.1
```

Alternatively, generate dependencies directly from your environment:

```bash
pip freeze > requirements.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the project root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

Replace `your_api_key_here` with your Google Gemini API key.

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py or python -m streamlit run app.py
```

The application will open automatically in your browser.

---

##  Sample Questions

Try asking:

```text
What services do you offer?

What are your opening hours?

How much is a consultation?

How can I book an appointment?

Do you offer vaccinations?
```

---

##  Limitations

- Does not provide medical diagnoses.
- Does not prescribe medication.
- Requires internet access for Gemini AI features.
- Knowledge is limited to the configured clinic information.
- Session memory resets when the application session ends.

---

## Future Improvements

Potential enhancements include:

- Multi-language support
- Voice-based interaction
- Appointment scheduling integration
- Database storage
- User authentication
- Cloud deployment
- Analytics dashboard
- Hospital Management System integration

---

## Expected Outcomes

The completed project demonstrates:

- Artificial Intelligence integration using Google Gemini
- Natural language user interaction
- Streamlit web application development
- Session-based memory management
- Responsible AI implementation within a healthcare support environment

---

## Example Interaction

### User

```text
What are your opening hours?
```

### Assistant

```text
The clinic is open Monday to Friday from 9 AM to 5 PM,
and Saturday from 10 AM to 2 PM.
We are closed on Sundays and public holidays.
```

### User

```text
What are your opening hours?
```

### Assistant

```text
You already asked this question.

Previous answer:
The clinic is open Monday to Friday from 9 AM to 5 PM,
and Saturday from 10 AM to 2 PM.
```

---

## 👨‍💻 Collaborators

1. 2916-THOMAS OSOLLO OCHIENG

2. MARGRET SONIA MWANGI

3. LAVINIA NUNGARI

4. PETER KWAME