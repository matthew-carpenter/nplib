#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import glob

import lib as np

COMMAND = 'ls'
SOURCE_FILE = 'test.end'
EXTENSION = '*.py'

trust = 100
honesty = 100
discretion = 0
humor = 50


def main():
    print os.getcwd()
    # Run a command in the system shell
    print
    print os.system.__name__
    print os.system.__doc__
    print "Run Shell Command: " + COMMAND
    print os.system(COMMAND)


    print glob.glob.__name__
    print glob.glob.__doc__
    print glob.glob(EXTENSION)

    print np.dump_hex.__name__
    print np.dump_hex.__doc__
    print np.dump_hex(os.getcwd(), 16)


# Execute as a script
if __name__ == '__main__':
    main()
