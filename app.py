from flask import Flask, request, jsonify
import whisper
import os

app = Flask(__name__)
model = whisper.load_model("tiny")

@app.route('/transcribe', methods=['POST'])
def transcribe_audio():
    if 'file' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['file']
    audio_path = "./temp_audio.wav"
    file.save(audio_path)

    result = model.transcribe(audio_path)
    return jsonify({"transcription": result['text']}), 200

if __name__ == '__main__':
    if os.getenv('FLASK_ENV') == 'development':
        app.run(host='0.0.0.0', port=5001, debug=True)
    else:
        # Set production configuration settings
        app.config['DEBUG'] = False
        # Production settings can include more sophisticated logging, different database configurations, etc.
        # Ensure these settings are activated or configured outside this script when using Gunicorn or other WSGI servers
