import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "name": "John Doe",
        "age": 32,
        "city": "New York",
        "is_student": False,
        "grades": [85, 90, 78]
    }
    return data


if __name__ == '__main__':
    app.run()
