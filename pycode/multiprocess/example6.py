import multiprocessing
import time
import sys

def daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    time.sleep(2)
    print 'Exiting:', p.name, p.pid

def non_daemon():
    p = multiprocessing.current_process()
    print 'Starting:', p.name, p.pid
    print 'Exiting:', p.name, p.pid

if __name__ == '__main__':
    d = multiprocessing.Process(name='daemon', target=daemon)
    d.daemon = True

    n = multiprocessing.Process(name='non-daemon', target=non_daemon)
    n.daemon = False;

    d.start()
    n.start()

    d.join(1)
    print 'd.is_alive()', d.is_alive()
    n.join()
