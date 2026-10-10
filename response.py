import requests
import os
from dotenv import load_dotenv

URL = "https://generativelanguage.googleapis.com/v1beta/interactions"

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
HEADERS = {
    "x-goog-api-key": API_KEY,
    "Content-Type": "application/json"
}

# ----------AI Response--------------#

def gen_output(text):
    payload = {
        "model": "gemini-3.1-flash-lite",
        "input": text
    }
    response = requests.post(URL, headers=HEADERS, json=payload)
    return response.json()
