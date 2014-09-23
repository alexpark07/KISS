from app import app
from flask import render_template, flash, redirect, session, url_for, request, g

from ARMSCGen import *
from app import status

@app.route('/')
@app.route('/index')
def index():
    sc = status.getStatus()

    return render_template('index.html', 
        title = 'Home', 
        result = sc['html'], 
        thumb = sc['thumb'],
        arm = sc['arm'],
        arm64 = sc['arm64'])

@app.route('/thumb/<scodename>')
@app.route('/thumb')
def thumb_func(scodename=None):
    if scodename is None:
        sc = status.getStatus()

        return render_template('thumb.html', 
            title = 'Thumb Mode', 
            result = sc['html'], 
            thumb = sc['thumb'])
    else:
        show = getShellcodeHelp(scodename, 'thumb')
        return render_template('shellcodeInfo.html', 
            title = 'Thumb Mode', 
            scodename = scodename,
            mode  = 'thumb',
            result = show)

@app.route('/arm')
@app.route('/arm/<scodename>')
def arm_func(scodename=None):
    if scodename is None:
        sc = status.getStatus()

        return render_template('arm.html', 
            title = 'ARM Mode', 
            result = sc['html'], 
            arm = sc['arm'])
    else:
        show = getShellcodeHelp(scodename, 'arm')
        return render_template('shellcodeInfo.html', 
            title = 'ARM Mode', 
            scodename = scodename,
            mode  = 'arm',
            result = show)

@app.route('/arm64')
@app.route('/arm64/<scodename>')
def arm64_func(scodename=None):
    if scodename is None:
        sc = status.getStatus()

        return render_template('arm64.html', 
            title = 'ARM64 Mode', 
            result = sc['html'], 
            arm64 = sc['arm64'])
    else:
        show = getShellcodeHelp(scodename, 'arm64')
        return render_template('shellcodeInfo.html', 
            title = 'ARM64 Mode', 
            scodename = scodename,
            mode  = 'arm64',
            result = show)
