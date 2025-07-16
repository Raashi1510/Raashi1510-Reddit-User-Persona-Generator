import os
import time
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

def generate_persona(username, user_data):
    try:
        api_key = os.getenv("GEMINI_API_KEY")
        if not api_key:
            raise ValueError("GEMINI_API_KEY is missing from .env")

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")  # Lower quota model

        input_text = "\n".join(user_data["posts"][:10] + user_data["comments"][:10])  # Reduce data
        prompt = (
            f"Analyze this Reddit user's persona briefly (keep response short):\n\n"
            f"USER: u/{username}\n"
            f"CONTENT:\n{input_text}\n\n"
            "Summarize in 5 bullet points."
        )

        time.sleep(5)  # Rate limiting
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        print(f"[ERROR] LLM generation failed: {e}")
        return "Persona generation failed."



