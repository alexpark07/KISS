#!python
# code from http://stackoverflow.com/questions/3160699/python-progress-bar

import time
import sys 


def doing_something():
    time.sleep(0.1)

def runner():
    toolbar_width = 40

    sys.stdout.write('[%s]' % (' ' * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write('\b' * (toolbar_width+1))

    for i in xrange(toolbar_width):
        doing_something()
        sys.stdout.write('#')
        sys.stdout.flush()

    sys.stdout.write('\n')
    sys.stdout.write('done\n')

if __name__ == '__main__':
    runner()
