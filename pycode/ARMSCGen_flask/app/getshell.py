from ARMSCGen import *

def _string(s):
    out = []
    for c in s:
        co = ord(c)
        out.append('\\x%02x' % co)
    return '"' + ''.join(out) + '"\n'

def _carray(s):
    out = []
    for c in s:
        out.append('0x' + enhex(c))
    return '{' + ', '.join(out) + '};\n'

def enhex(c):
    return c.encode('hex')

def unhex(c):
    return c.decode('hex') 

def get(arch, sname, opt, fm, xor):
    thgen    = thumbSCGen()
    armgen   = armSCGen()
    arm64gen = arm64SCGen()

    fms = []
    args = opt.split()
    for i in range(0, len(args)):
        fms.append( "'%s'" % (args[i]) )

    scode = sname + "(" + ','.join(fms) + ")"

    try:
        if arch == 'arm':
            show = eval("armgen.%s" % (scode))
            prepareCompiler('ARM')
        elif arch == 'arm64':
            show = eval("arm64gen.%s" % (scode))
            prepareCompiler('ARM64')
        elif arch == 'thumb':
            show = eval("thgen.%s" % (scode))
            prepareCompiler('THUMB')

        if fm == 'asm':
            return show
        else:
            scode = CompileSC(show)
            xscode = ''
            if xor != u'0':
                if arch != 'arm64':
                    xscode = MakeXorShellcode( scode )
            if len(xscode) != 0:
                scode = xscode

            if fm == 'c':
                return _carray(scode)
            elif fm == 'string':
                return _string(scode)
            elif fm == 'raw':
                return scode
            elif fm == 'hex':
                return enhex(scode)
            else:
                return _string(scode)

    except AttributeError:
        return "There is no '%s' shellcode so far" % (args[0])
    except:
        return "I think, you have wrong options. show shellcode for you"

    return 'There is no result'
