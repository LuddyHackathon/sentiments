import os
from flask import Flask, request, jsonify
import requests

from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# Hugging Face Inference API details
API_URL = 'https://api-inference.huggingface.co/models/bhadresh-savani/distilbert-base-uncased-emotion'
headers = {
    'Authorization': f'Bearer {os.environ.get('HF_TOKEN')}'
}


def get_emotion(text):
    payload = {'inputs': text}
    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()
    else:
        return {'error': f'Status {response.status_code}', 'details': response.text}


@app.route('/', methods=['POST'])
def analyze_sentiment():
    text = request.args.get('text')

    if not text:
        return jsonify({"error": "Missing 'text' in query parameters"}), 400

    result = get_emotion(text)
    return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=65535, debug=True)
