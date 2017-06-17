#!/usr/bin/python
# -*- coding: utf-8 -*-

# Standard Library imports
import os
from datetime import datetime

# Third party imports
import requests

# Old Masters imports
import lib as np

LOGMODE = 'overwrite'
LOGFILE = 'debug.log'
LOGLEVEL = 'DEBUG'

gituser = raw_input("Username: ")
gitpass = raw_input("Password: ")

# Set up logger
np.init_logging(LOGMODE, LOGLEVEL, LOGFILE)


c = ""
cwd = c.join(["Directory: ", os.getcwd()])
np.logging.debug(cwd)


r = requests.get('https://api.github.com/user', auth=(gituser, gitpass))

print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()


def main():
    np.logging.debug(" %s function started: -- %s " % (main.__name__, str(datetime.now())))


if __name__ == '__main__':
    np.logging.debug(" Starting %s as a script: -- %s", os.path.basename(__file__), str(datetime.now()))
    main()
