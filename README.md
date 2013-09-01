pyexec README
=============

This is a small application to paste/type a python snippet and execute it.
Useful for ad-hoc testing of smaller code fragments without much setup. Just
paste and run.

### Usage

1.  paste or type python snipet in input box
2.  run application with the run control (or Alt-r)
3.  see result in the output box

#### X11 Clipboard Fetch Startup

1.  run ./pyexec.py -xclip
2.  see X11 clipboard content in input and result in output

### Requirements

*   Linux       -- tested on Ubuntu 12.04
*   Python 3    -- it's a python 3 script
*   PySide      -- tested with 1.1.0, package python3-pyside in Ubuntu

### Features

*   save input to file in temp folder and run it
*   output result in output box
*   highlight stderr output red
*   put return code in the return code field

