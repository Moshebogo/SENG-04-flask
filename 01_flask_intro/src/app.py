from flask import Flask


app = Flask(__name__)

@app.route("/")
def root():
    return '<h1> Welcome to my Flask Aplication! </h1>'

if __name__ == '__main__':
    app.run(debug = True, port = 8000, host = '127.0.0.1')