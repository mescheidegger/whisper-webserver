## Third-Party Dependencies
This project uses third-party libraries and external APIs (e.g., OpenAI). Their respective licenses and terms of service apply. This project is licensed under MIT, but usage of third-party services must comply with their own terms.

This project contains an implementation for the open source AI transcription service Whisper.

This code can be deployed as a part of a project following general micro-service architecture.

Using a .env file you can create / issue API keys for use by other separately hosted applications.

To update the model used change the following line in app.py:

model = whisper.load_model("tiny")

Workflow wise you would create a web application that records audio through the browser, post it to the endpoint hosted by this server, and receive back transcribed audio.

Requirements:
1. ffmpeg must be installed on the webserver
2. create a .env file and create an API key
3. To run in development mode: set FLASK_ENV=development && python app.py
4. To run in production mode: gunicorn "app:app" --bind 0.0.0.0:5001
