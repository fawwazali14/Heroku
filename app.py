import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "name": "John Doe",
        "age": 97,
        "city": "New York",
        "is_student": False,
        "grades": [85, 90, 78]
    }
    return data

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use port provided by Heroku or default to 5000
    app.run(host='0.0.0.0', port=port)
