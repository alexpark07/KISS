#!python

from progressbar import *

progress = ProgressBar()

for i in progress(range(80)):
    time.sleep(0.01)
