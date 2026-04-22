"""Flask server for Emotion Detector"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/")
def index():
    """Render home page"""
    return render_template("index.html")


@app.route("/emotionDetector")
def detect():
    """Handle emotion detection"""
    text = request.args.get("text")

    # error handling wajib (HARUS PERSIS)
    if not text:
        return "Invalid input! Try again."

    result = emotion_detector(text)

    # kalau API gagal
    if result is None:
        return "Error processing request"

    # format output HARUS seperti ini
    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(debug=True)