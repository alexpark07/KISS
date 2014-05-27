def trans_str(s):
    mod = len(s) % 4
    ran = len(s) / 4
    txt = []
    j = 0
    for i in range(0, ran):
        t  = s[j+3]
        t += s[j+2]
        t += s[j+1]
        t += s[j+0]
        j += 4
        txt.append('push 0x%s' % t.encode('hex').ljust(8, '0'))
    txt.append('push 0x%s' % s[j:j+mod].encode('hex').ljust(8, '0'))
    txt.reverse()
    return txt

print trans_str('/etc/passwd')
