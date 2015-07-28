#!python

import socket
import ssl

HOST = '192.168.10.10'
PORT = 31337

# CREATE SOCKET
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.settimeout(10)

# WRAP SOCKET
s_sock = ssl.wrap_socket(sock, ssl_version=ssl.PROTOCOL_TLSv1, ciphers="ADH-AES256-SHA")

# CONNECT AND PRINT REPLY
s_sock.connect((HOST, PORT))
pkt = '''payload'''
s_sock.send(pkt)
print s_sock.recv(1280)

# CLOSE SOCKET CONNECTION
s_sock.close(
