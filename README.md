# mutual-tls

Simple implementation of Mutual TLS in Python using [requests](https://docs.python-requests.org/en/master/index.html) and [Flask](https://flask.palletsprojects.com).

Generate certificates:
```
$ bash generate_certs.sh
```

Start the server:
```
$ pip install -r requirements.txt
$ python3 server.py
```

Hit it:
```
$ python3 client.py
```
