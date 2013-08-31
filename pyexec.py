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
import time

from PySide.QtCore    import *
from PySide.QtGui     import *
from PySide.QtUiTools import *

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

app = QApplication(sys.argv)

loader = QUiLoader()
uifile = QFile('root.ui')
uifile.open(QFile.ReadOnly)

root_window = loader.load(uifile)

uifile.close()

root_window.show()
sys.exit(app.exec_())

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

