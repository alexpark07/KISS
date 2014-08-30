# find a peer

def generate():
    """find a socket, which is connected to the specified port in thumb mode
    Leaves socket in r0 reg.

    argument:
        port (int/str): specific port

    backup:
        r6: indicates found socket/file descriptor
    """

    sc = """
findpeer_1:
    sub r5, r5, r5
    add r5, r5, #-1
    mov r3, sp
looplabel_2:
    mov sp, r3
    add r5, r5, #1
    mov r0, r5
    movs r2, #4
    push {r2}
    mov r2, sp
    add r1, sp, #32
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #32
    svc 1
    cmp r0, #0
    bne looplabel_2
    mov r6, r5
    """
    return sc

if __name__ == '__main__':
    print generate()
