import requests

host = 'localhost'
port = 5000

def plain_http():
    url = f'http://{host}:{port}'
    response = requests.get(url)
    print(response)
    print(response.text)

def client_verifies_server():
    https = f'https://{host}:{port}'
    response = requests.get(https, verify='server.crt')
    print(response)
    print(response.text)

# print('Sending request with plain http...')
# plain_http()

print('Sending request with https...')
client_verifies_server()
