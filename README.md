# Chat Summary Generator API (Django + LLM)

This Django-based backend service accepts a sequence of user and bot messages, processes the chat using a Large Language Model (LLM), and returns a concise **summary** of the entire conversation. This API is **production-ready**, modular, and testable using **Postman** or **cURL**.

---

## Features

- Accepts structured chat conversations (user + bot messages)
- Generates accurate summaries using LLMs (e.g., OpenAI GPT)
- RESTful API powered by **Django REST Framework**
- Unit tested with Django's test framework
- Easily testable using **Postman** or **cURL**

---

## Setup Instructions

Follow the steps below to set up the project on your local machine:

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/Chat-Summary-Generator.git
cd Chat-Summary-Generator
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run Development Server

```bash
python manage.py runserver
```

The server will start at: `http://127.0.0.1:8000/`

---

## 🧪 Running Tests

To run unit tests for the `summarizer` app:

```bash
python manage.py test summarizer
```

---

## 📬 API Usage

### Endpoint

```
POST /api/summarize/
```

### Request Body (JSON)

```json
{
  "chat": [
    {"sender": "user", "message": "Hi, I want to book a flight to Delhi."},
    {"sender": "bot", "message": "Sure. What date are you planning to travel?"},
    {"sender": "user", "message": "This Friday."},
    ...
  ]
}
```

### Response

```json
{
  "summary": "User wanted to book a flight to Delhi for Friday. Bot asked for travel details."
}
```

### Testing via cURL

```bash
curl -X POST http://127.0.0.1:8000/api/summarize/ \
  -H "Content-Type: application/json" \
  -d '{"chat": [{"sender": "user", "message": "Hi"}, {"sender": "bot", "message": "Hello!"}]}'
```

---

