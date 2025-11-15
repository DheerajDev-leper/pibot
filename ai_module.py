import requests
import json
from config import OPENAI_API_KEY, OPENAI_API_URL

def ask_gpt(question):
    """Send question to GPT and return answer."""
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": question}],
        "temperature": 0.7
    }
    response = requests.post(OPENAI_API_URL, headers=headers, data=json.dumps(data))
    if response.status_code == 200:
        answer = response.json()['choices'][0]['message']['content']
        return answer
    else:
        print("Error:", response.status_code, response.text)
        return "Sorry, I could not get an answer."
