import os
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL_NAME = "llama-3.3-70b-versatile"
MAX_TOKENS = 1000
SYSTEM_PROMPT = "You are a helpful and friendly AI assistant."
APP_TITLE = "My AI Chatbot"
APP_ICON = "🤖"