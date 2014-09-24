import markdown
from app import app
from flask import render_template, flash, redirect, session, url_for, request, g
from flask import Markup

from ARMSCGen import *
from app import status
from app import getshell

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

@app.route('/help')
def help_func():
    result = """

/*
    For more information: <a href="http://armscgen.readthedocs.org/">Here</a>
*/

$ scgen -h

Please choice one of shellcodes to show you
Usage: scgen [options]

ARM32/64 shellcodes by alex.park

Options:
  -h, --help            show this help message and exit
  -a ARCH, --architechture=ARCH
                        ARM Archtechture (default: arm32 thumb) options:
                        thumb, arm, arm64
  -?, --show            Show shellcode documentation
  -l, --list            List all the shellcodes if arch is "all"
  -f FORMAT, --format=FORMAT
                        {r}aw, {s}tring, {h}ex, {a}sm, {c} for C code
  -x XOR, --xor=XOR     XOR Encoder if you want to avoid bad chars like 0x00,
                        0x0a and so on Notice: only for arm32, thumb
                        shellcodes so far
"""
    return render_template('help.html', title='Help', result=result)


@app.route('/about')
def about_func():
    result = """
### Shellcodes for ARM/Thumb mode

Ideas came from [shell-storm](http://www.shell-storm.org) and [pwntools/pwnies](https://github.com/Gallopsled/pwntools).
Thanks to share all of brilliant sources on the net.
I'm interested in mobile platform and archtecture like Android on ARM, Router on MIPS and so on.
This project named ARMSCGen focus on shellcode on ARM Architecture especially ARMv7 Thumb Mode.

### Requirement

Cross Compile Tool for ARM
``as``, ``ld`` and ``objcopy``
capstone to disassemble codes
URL: ``http://www.capstone-engine.org/``

### Installation
``python setup.py install``

### Usage
reads ``examples`` directory
and
uses ``scgen.py`` in CLI mode

### List of Shellcodes 
please refer to ``shellcodes_lists.md`` or ``scgen -l -a all``

### Documentation
URL: ``http://armscgen.readthedocs.org/`` or ``/docs/`` in source

### TODO
``AArch32-ARM Mode`` shellcodes

(To be continued)
"""

    rv = Markup(markdown.markdown(result))
    return render_template('help.html', title='About', result=rv)
    

@app.route('/thumb')
@app.route('/thumb/<scodename>', methods=['POST', 'GET'])
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

@app.route('/makeShellcode', methods=['POST'])
def makeShellcode_func():
    scodename = request.form['scodename']
    arch      = request.form['arch']
    opts      = request.form['option']
    fms       = request.form['format']
    xor       = request.form['xoring']

    # get(arch, sname, opt):
    rv = getshell.get(arch, scodename, opts, fms, xor)

    return rv
