# send a file
def generate(in_fd, out_fd):
    """sends a file to user in thumb mode

    Args: 
        in_fd  (str/iny): in file descriptor
        out_fd (str/iny): out file descriptor
    """

    if isinstance(in_fd, int):
        sc = "mov r0, #%s" % (in_fd)
    else:
        sc = "mov r0, %s" % (in_fd)

    sc += """
    mov r1, #%s
    sub r2, r2, r2
    mov r3, #255
    mov r7, #(0+187)
    svc 1
    """ % (out_fd)
    return sc
