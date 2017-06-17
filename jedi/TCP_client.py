# -*- coding: utf-8 -*-

import os
import socket

# define some constants
TARGET_HOST = "www.google.com"
TARGET_PORT = 80
PAYLOAD = "GET / HTTP/1.1\r\nHost: " + TARGET_HOST + "\r\n\r\n"
RESPONSE_FILE = 'response.txt'

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to the web server
s.connect((TARGET_HOST, TARGET_PORT))

# send some data
s.send(PAYLOAD)

# receive some data
response = s.recv(4096)

with open(RESPONSE_FILE, 'w') as f:
    f.write(response)

print
print "Simple TCP Client: Starting..."
print
print "Current working directory: " + os.getcwd()
print
print "Target Host: " + TARGET_HOST
print "Target Port: " + str(TARGET_PORT)
print
print "[+] Response: Written to " + RESPONSE_FILE
