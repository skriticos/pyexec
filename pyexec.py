#! /usr/bin/env python3
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# (c) 2013, Sebastian Bartos <sebastian.bartos@gmail.com>
#           Terms of the general public license (GPL) version 2 or later apply.
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
# Control names
#
#     btn_run
#     l_exit_code
#     l_input
#     l_output
#     txt_exit_code
#     txt_input
#     txt_output
#     w_controls
#     w_input
#     w_input_output
#     w_output
#     w_root
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import sys
import tempfile
import subprocess

from PySide.QtCore    import *
from PySide.QtGui     import *
from PySide.QtUiTools import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def run():

    root_window.txt_output.clear()
    root_window.txt_exit_code.clear()

    with tempfile.TemporaryDirectory() as tmpdirname:

        execname = os.path.join(tmpdirname, 'run.py')
        with open(execname, 'w') as f:
            f.write(root_window.txt_input.toPlainText())

        proc = subprocess.Popen(
            ['/usr/bin/env', 'python3', execname],
            cwd=tmpdirname,
            shell=False,
            close_fds=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
            )

        while proc.poll() is None:

            lines = proc.stdout.readlines()
            proc.stdout.flush()
            if lines:
                txt = root_window.txt_output.toHtml()
                for line in lines:
                    txt += line.decode('utf-8') + '<br>'
                root_window.txt_output.clear()
                root_window.txt_output.setHtml(txt)

            lines = proc.stderr.readlines()
            proc.stderr.flush()
            if lines:
                txt = root_window.txt_output.toHtml()
                for line in lines:
                    txt += '<span style="color:red">{}</span>'.format(line.decode('utf-8')) + '<br>'
                root_window.txt_output.clear()
                root_window.txt_output.append(txt)

        ret = proc.wait()
        root_window.txt_exit_code.setText(str(ret))

app = QApplication(sys.argv)

loader = QUiLoader()
uifile = QFile('root.ui')
uifile.open(QFile.ReadOnly)
root_window = loader.load(uifile)
uifile.close()

shortcut = QShortcut('Ctrl+w', root_window)
shortcut.activated.connect(root_window.close)

root_window.btn_run.clicked.connect(run)

root_window.show()

# if we start with ./pyexec.py -xclip, the input box should be filled with the
# current X11 clipboard and run
if sys.argv[1] == '-xclip':

    proc = subprocess.Popen(['/usr/bin/xsel', '--clipboard'],
                         shell = False, stdout = subprocess.PIPE)

    while proc.poll() is None:

        lines = proc.stdout.readlines()
        proc.stdout.flush()
        if lines:
            for line in lines:
                txt = line.decode('utf-8')
                if txt[-1] == '\n':
                    txt = txt[:-1]
                root_window.txt_input.appendPlainText(txt)

    proc.wait()
    run()
    root_window.showMaximized()

    p = root_window.w_input.sizePolicy()
    p.setVerticalStretch(0)
    root_window.w_input.setSizePolicy(p)
    p = root_window.w_output.sizePolicy()
    p.setVerticalStretch(2)
    root_window.w_output.setSizePolicy(p)

sys.exit(app.exec_())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

