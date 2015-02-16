#!python
#-*- coding: utf-8 -*-
# code from internet

from hexdump import hexdump
import socket
import telnetlib
import struct

HOST = ''
PORT = 31337


def P(value, fm):
	ret = []
	if type(value) == list or type(value) == tuple:
		for v in value:
			ret.append(struct.pack(fm, v))
		return ret
	else:
		return struct.pack(fm, value)

def U(value, fm):
	ret = []
	if type(value) == list or type(value) == tuple:
		for v in value:
			ret.append(struct.unpack(fm, v))
		return ret
	else:
		return struct.unpack(fm, value)

def interact(sock):
	t = telnetlib.Telnet()
	t.socket = sock
	t.interact()


def r_until(sock, st, debug=False):
	ret = ''
	while st not in ret:
		lret = sock.recv(8192)
		if debug and len(lret) > 0:
			print repr(lret)
		ret += lret
	return ret

if __name__ == '__main__':

	s = socket.create_connection((HOST, PORT))
	print r_until('until_message')

	print "Interactive shell"
	interact(s)
