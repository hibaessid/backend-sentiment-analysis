from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)

# Load pre-trained sentiment analysis model
sentiment_analysis = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

# Serve the frontend index.html
@app.route('/')
def serve_frontend():
    return send_from_directory('../frontend', 'index.html')

# Define the sentiment analysis endpoint
@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    data = request.json
    text = data.get('text', '')
    if text:
        result = sentiment_analysis(text)[0]
        return jsonify({"label": result['label'], "score": result['score']})
    return jsonify({"error": "No text provided"}), 400

if __name__ == "__main__":
    app.run(debug=True)
