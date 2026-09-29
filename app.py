import os
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import google.generativeai as genai
from chatbot_config import SYSTEM_PROMPT

load_dotenv()

app = Flask(__name__)
API_KEY = os.getenv("GEMINI_API_KEY")

if API_KEY:
    genai.configure(api_key=API_KEY)

MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-2.0-flash")

def generate_reply(user_message):
    if not API_KEY:
        return "Gemini API key is not configured. Add GEMINI_API_KEY to your environment variables."

    model = genai.GenerativeModel(
        MODEL_NAME,
        system_instruction=SYSTEM_PROMPT
    )
    response = model.generate_content(user_message)
    return getattr(response, "text", "") or "Sorry, I could not generate a response."

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    message = (data.get("message") or "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message."}), 400

    try:
        reply = generate_reply(message)
        return jsonify({"reply": reply})
    except Exception as exc:
        return jsonify({"reply": f"Sorry, an error occurred: {str(exc)}"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.getenv("PORT", 5000)), debug=True)
