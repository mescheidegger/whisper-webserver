from flask import Flask, request, jsonify
from dotenv import load_dotenv
import whisper
import os
import logging

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)
model = whisper.load_model("tiny")

API_KEY = os.getenv("API_KEY")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    logging.info("Received request to transcribe audio.")
    
    # Check for API key in the request header
    api_key = request.headers.get('x-api-key')
    if api_key != API_KEY:
        logging.warning("Unauthorized access attempt with API key: {}".format(api_key))
        return jsonify({"error": "Unauthorized access"}), 401

    if 'file' not in request.files:
        logging.error("No file part in the request.")
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    audio_path = "./temp_audio.wav"
    file.save(audio_path)
    logging.info(f"Saved file to {audio_path}")

    result = model.transcribe(audio_path)
    logging.info("Transcription completed.")
    return jsonify({"transcription": result['text']}), 200

if __name__ == '__main__':
    logging.info("Starting Flask application...")
    if os.getenv('FLASK_ENV') == 'development':
        app.run(host='0.0.0.0', port=5001, debug=True)
    else:
        app.config['DEBUG'] = False
        app.run(host='0.0.0.0', port=5001)
