from app import app
from flask import render_template, flash, redirect, session, url_for, request, g

from ARMSCGen import *

@app.route('/')
@app.route('/index')
def index():

    sc = {}
    sc['thumb'] = getShellcodeInfo('thumb')
    sc['arm']   = getShellcodeInfo('arm')
    sc['arm64'] = getShellcodeInfo('arm64')
    
    result = '''
by arch
-------
<a href="/thumb">Thumb</a> Mode: %s
<a href="/ARM">ARM</a>   Mode: %s
<a href="/ARM64">ARM64</a> Mode: %s''' % (len(sc['thumb']), len(sc['arm']), len(sc['arm64']))

    result += '''
by list
-------
'''
    return render_template('index.html', 
        title = 'Home', 
        result = result, 
        thumb = sc['thumb'],
        arm = sc['arm'],
        arm64 = sc['arm64'])
