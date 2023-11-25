from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, this is your Flask endpoint!'

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Use 5000 as default if PORT is not set
    app.run(debug=True, port=port)