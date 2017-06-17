#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging
import thread
import threading


try:
    import requests
except ImportError:
    requests = None


__title__ = 'nplib'
__version__ = '0.00.1'
__build__ = 0001
__author__ = 'Matthew Lee Carpenter'
__license__ = 'GPL 3.0'
__copyright__ = '(C) Copyright 2017 Matthew Lee Carpenter'


# ---------------------------------------------------------------------------
#  Miscellaneous module data
# ---------------------------------------------------------------------------
