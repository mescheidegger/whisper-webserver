1. To run in development mode: 

set FLASK_ENV=development && python app.py

2. To run in production mode:

gunicorn "app:app" --bind 0.0.0.0:5001


3. ffmpeg must be installed on the webserver
