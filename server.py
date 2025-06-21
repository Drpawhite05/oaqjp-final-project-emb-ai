from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask(__name__)

# Define route for emotion detection
@app.route("/emotionDetector", methods=["GET"])
def detect_emotion():
    # Get text from query parameter
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Validate input
    if not text_to_analyze:
        return jsonify({"error": "Missing textToAnalyze parameter"}), 400

    # Call emotion detector function
    result = emotion_detector(text_to_analyze)

    # Return result as JSON
    return jsonify(result)

# Run the app
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
