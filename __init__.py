#!/usr/bin/python
# -*- coding: utf-8 -*-

# Set default logging handler to avoid "No handler found" warnings.
import logging

try:  # Python 2.7+
    from logging import NullHandler
except ImportError:
    class NullHandler(logging.Handler):
        def emit(self, record):
            pass

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

logging.getLogger(__name__).addHandler(NullHandler())

# ---------------------------------------------------------------------------
#  MODULE DATA
