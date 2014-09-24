from app import app
from ARMSCGen import *

def getStatus():

    sc = {}
    sc['thumb'] = getShellcodeInfo('thumb')
    sc['arm']   = getShellcodeInfo('arm')
    sc['arm64'] = getShellcodeInfo('arm64')
    
    result = '''by arch
-------
<a href="/thumb">Thumb</a> Mode: %s
<a href="/arm">ARM</a>   Mode: %s
<a href="/arm64">ARM64</a> Mode: %s''' % (len(sc['thumb']), len(sc['arm']), len(sc['arm64']))

    result += '''

by list
-------'''
    sc['html'] = result    
    return sc
