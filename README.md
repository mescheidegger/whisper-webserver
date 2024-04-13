1. ffmpeg must be installed on the webserver

2. create a .env file and create an API key

3. To run in development mode: set FLASK_ENV=development && python app.py

4. To run in production mode: gunicorn "app:app" --bind 0.0.0.0:5001
