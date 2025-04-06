import os
import requests
import json

from dotenv import load_dotenv

load_dotenv()

API_URL = 'https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion'
headers = {
    'Authorization': f'Bearer {os.environ.get('HF_TOKEN')}'
}

def query(text: str):
    payload = {'inputs': text}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()

# ✅ Example usage
if __name__ == '__main__':
    input_text = 'The team is excited but nervous about the launch.'
    result = query(input_text)
    print(json.dumps(result, indent=2))