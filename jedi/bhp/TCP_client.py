# -*- coding: utf-8 -*-

import socket

target_host = "mozilla.org"
target_port = 80

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect the client
client.connect((target_host, target_port))

# send some data
client.send("GET / HTTP/1.1\r\nHost: mozilla.org\r\n\r\n")

# receive some data
response = client.recv(4096)

print
print "Simple TCP Client: Starting..."
print
print "Target Host: " + target_host
print "Target Port: " + str(target_port)
print
print "[+] Response:"
print
print response
