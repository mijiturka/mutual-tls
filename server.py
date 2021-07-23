from flask import Flask

app = Flask(__name__)

@app.route('/')
def endpoint():
    return "You've reached the server"

def serve_over_http():
    app.run()

def serve_over_https():
    app.run(ssl_context=('server.crt', 'server.key'))

if __name__ == '__main__':
    serve_over_https()
