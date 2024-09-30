from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from transformers import pipeline

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load pre-trained sentiment analysis model
sentiment_analysis = pipeline('sentiment-analysis', model="distilbert-base-uncased-finetuned-sst-2-english")

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
