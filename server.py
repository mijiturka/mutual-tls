from flask import Flask

app = Flask(__name__)

@app.route('/')
def endpoint():
    return "You've reached the server"
