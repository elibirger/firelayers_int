#!/bin/bash
filename='domains'
echo Start
while read DOMAIN; do 
   openssl genrsa -out intermediate/private/$DOMAIN.key.pem 2048
   chmod 400 intermediate/private/$DOMAIN.key.pem
   openssl req -config ./<file>.cnf -subj '/C=IL' -new -key intermediate/private/$DOMAIN.key.pem -out intermediate/csr/$DOMAIN.key.pem
   openssl ca -batch -config ./<file>.cnf -subj '/CN=*.'$DOMAIN'/O=<org>/OU=<org unit>/C=<country>/ST=<state>' -days 3650 -in intermediate/csr/$DOMAIN.key.pem -passin pass:<password> -out intermediate/certs/$DOMAIN.cert.pem 
done < $filename
