# exit(n)

def generate(n=0):
    sc = "\n"
    if n != 0:
        sc += "mov r0, #%s" % int(n)
    else:
        sc += "sub r0, r0, r0"

    sc += """
    mov r7, #1
    svc 1
    """
    return sc

if __name__ == '__main__':
    print generate()
