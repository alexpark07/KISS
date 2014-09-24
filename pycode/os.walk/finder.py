#!/usr/bin/python
# http://stackoverflow.com/questions/16953842/using-os-walk-to-recursively-traverse-directories-in-python

import os
import sys

# traverse root directory, and list directories as dirs and files as files
start = '.'
if len(sys.argv) != 1:
    start = sys.argv[1]

tf = 'hello_world_XXX.txt'

for root, dirs, files in os.walk(start):
    try:
        f = '%s/%s' % (root, tf)
        open(f, 'wb').write('x')
        if os.path.exists(f) == True:
            print "Found: %s" % (root)
            os.unlink(f)
    except:
        pass
        
    #path = root.split('/')
    #print (len(path) - 1) *'---' , os.path.basename(root)
    #for file in files:
    #    print len(path)*'---', file
