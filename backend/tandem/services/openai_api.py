import json
import os
from pathlib import Path

import requests
from dotenv import load_dotenv


def openai_request(user_message):
    BASE_DIR = Path(__file__).resolve().parents[2]
    load_dotenv(BASE_DIR / ".env")

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("OPENAI_API_KEY is missing. Add it to backend/.env.")

    url = "https://api.openai.com/v1/chat/completions"
    payload = json.dumps({
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "system",
                "content": "You are a native French speaker and a tandem conversation partner. When the user sends a message in French, first reply naturally and conversationally in French — like a real tandem partner would. Ask questions to keep the conversations going. Then, in a new paragraph starting with “CORRECTION:”, repeat only the user’s original sentence but corrected. Do not explain anything. Do not include the user’s original version. If the sentence was already correct, do not repeat it."
            },
            {
                "role": "user",
                "content": user_message,
            },
        ],
        "temperature": 0.7,
    })

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {OPENAI_API_KEY}",
    }

    response = requests.post(url, headers=headers, data=payload, timeout=30)
    print("OpenAI status:", response.status_code)
    print("OpenAI response body:", response.text)
    response.raise_for_status()
    data = response.json()

    return data["choices"][0]["message"]["content"]