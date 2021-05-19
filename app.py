from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello World!'

@app.route('/questions')
def questions():
    return 'Hello Questions!'

if __name__ == '__main__':
    app.run(debug=True)