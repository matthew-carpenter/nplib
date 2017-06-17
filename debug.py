#!/usr/bin/python
# -*- coding: utf-8 -*-

# Standard Library imports
import os
from datetime import datetime

# Third party imports


# Old Masters imports
import lib as np

LOGMODE = 'overwrite'
LOGFILE = 'debug.log'
LOGLEVEL = 'DEBUG'


# Set up logger
np.init_logging(LOGMODE, LOGLEVEL, LOGFILE)


c = ""
cwd = c.join([" Directory: ", os.getcwd()])
np.logging.debug(cwd)


def main():
    np.logging.debug(" %s function started: -- %s " % (main.__name__, str(datetime.now())))


if __name__ == '__main__':
    np.logging.debug(" Starting %s as a script: -- %s", os.path.basename(__file__), str(datetime.now()))

    main()
