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
cwd = c.join(["From: ", os.getcwd()])
np.logging.debug(cwd)


def main():
    np.logging.debug("%s function BEGIN ... " % main.__name__)


if __name__ == '__main__':
    np.logging.debug("Running %s as a script ..." % os.path.basename(__file__))
    main()
