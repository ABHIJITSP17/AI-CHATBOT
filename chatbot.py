from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def get_response(conversation_history):
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # free model
            messages=conversation_history,
            max_tokens=1000
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {str(e)}"