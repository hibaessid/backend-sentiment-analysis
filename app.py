from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# ML Model service URL
ML_MODEL_SERVICE_URL = "http://127.0.0.1:5001/predict"

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    if text:
        # Make an HTTP request to the ML model service
        response = requests.post(ML_MODEL_SERVICE_URL, json={"text": text})
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({"error": "Failed to get a response from the ML model"}), 500
    return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
