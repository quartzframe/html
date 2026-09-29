# Cooking Recipe AI

A focused LLM chatbot built with Flask and the Gemini API.

## Files
- `app.py` — Flask server and Gemini integration
- `templates/index.html` — complete responsive UI with CSS and JavaScript
- `chatbot_config.py` — domain-specific system prompt
- `requirements.txt` — Python dependencies
- `.env.example` — environment variable template
- `README.md` — setup instructions

## Run locally

1. Create a Gemini API key.
2. Copy `.env.example` to `.env`.
3. Put your key in `GEMINI_API_KEY`.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

5. Start:

```bash
python app.py
```

Open `http://localhost:5000`.

## Deploy
Use a Python web service and set:
`GEMINI_API_KEY=your_key`

Start command:
`gunicorn app:app`

The chatbot is intentionally domain-focused and should decline unrelated questions.
