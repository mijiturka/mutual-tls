#!/bin/bash

# Generate a certificate for the server

## Generate (unencrypted) key
## Flask does not support encrypted keys,
## so we can't set a password for the keys we'll be using for the server:
openssl genrsa \
  -out server.key 4096

## Generate certificate signing request
openssl req \
  -new \
  -config server.cnf \
  -key server.key \
  -out server.csr

## Generate certificate and sign it with the key
openssl x509 \
  -req \
  -days 7 \
  -in server.csr \
  -signkey server.key \
  -out server.crt

## Output the contents of the cert we've just created
# openssl x509 -noout -text -in server.cr


# Generate a certificate for the client

## Generate (unencrypted) key
## The Python requests module does not support encrypted keys,
## so we can't set a password for the keys we'll be using for the client:
## https://docs.python-requests.org/en/master/user/advanced/#client-side-certificates

# TODO
