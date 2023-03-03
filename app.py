import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/openai', methods=['POST'])
def openai():
    # Replace YOUR_API_KEY with your actual API key
    headers = {'Authorization': 'Bearer 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'}
    url = 'https://api.openai.com/v1/engines/davinci-codex/completions'

    # Get the prompt from the JSON payload
    prompt = request.json['prompt']

    # Send the prompt to the OpenAI API and get the response
    data = {
        'prompt': prompt,
        'max_tokens': 50,
        'n': 1,
        'stop': None,
    }
    response = requests.post(url, headers=headers, json=data)

    # Return the response as JSON
    return jsonify(response.json())

if __name__ == '__main__':
    app.run()
