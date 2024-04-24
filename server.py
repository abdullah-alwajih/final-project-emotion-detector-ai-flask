"""This module provides a Flask web server for an emotion detection service
using the Watson NLP API."""
from flask import Flask, request, jsonify, render_template

from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route('/')
def index():
    """Serve the homepage from the index.html template."""
    return render_template('index.html')


@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    """
    API endpoint for emotion detection.
    Accepts JSON input with 'text' key, analyzes it for emotions, and returns a formatted response.
    Returns an error message if no dominant emotion can be determined.
    """
    data = request.get_json() or {}
    text = data.get('text', '')
    result = emotion_detector(text)
    if result.get('dominant_emotion') is None:
        return jsonify("Invalid text! Please try again!"), 400

    response = (f"For the given statement, the system response is 'anger': {result['anger']}, "
                f"'disgust': {result['disgust']}, 'fear': {result['fear']}, 'joy': {result['joy']}, and "
                f"'sadness': {result['sadness']}. The dominant emotion is {result['dominant_emotion']}.")
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
