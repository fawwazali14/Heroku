from flask import Flask

app = Flask(__name__)

@app.route('/bye')
def bye_world():
    return 'Bye, World!'

if __name__ == '__main__':
    app.run()
