from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dotenv import load_dotenv
from tandem.models import Message        
import requests
import json
from openai import OpenAI
from django.db.models import Max
from uuid import UUID
from pathlib import Path
import os

def openai_request(user_message):
    
        BASE_DIR = Path(__file__).resolve().parent.parent
        load_dotenv(os.path.join(BASE_DIR, '.env'))
        
        OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    
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
                "content": user_message
                }
            ],
            "temperature": 0.7
            })
        
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + OPENAI_API_KEY,
            'Cookie': '__cf_bm=OFcuWiYUC1yGbKmIesyF1rE2Lu3psGajw45Y9EWv9U8-1744978447-1.0.1.1-Rz8ASBnoZfXYP0YzYp8yKWk1vq4gt4w2ROPvW75hTreZWaPCb1zwThjDDQYSiHIfoj8e0q5I2CA9LmsFmF3fMEANTwXdYguw__tRNyfO7Pc; _cfuvid=S3sGFsM07tmyr_e1xR2mz99UNa1j0N.sDQaEJdos2cw-1744964585928-0.0.1.1-604800000'
            }

        res = requests.request("POST", url, headers=headers, data=payload)
        data = res.json()

        reply= data["choices"][0]["message"]["content"]
        
        return reply