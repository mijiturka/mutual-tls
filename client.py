import requests

host = 'localhost'
port = 5000

def insecure():
    plain_http = f'http://{host}:{port}'
    response = requests.get(plain_http)
    print(response)
    print(response.text)

insecure()
