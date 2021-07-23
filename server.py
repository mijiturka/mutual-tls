from flask import Flask

app = Flask(__name__)

@app.route('/')
def endpoint():
    return "You've reached the server"

if __name__ == '__main__':
    app.run(ssl_context=('server.crt', 'server.key'))
