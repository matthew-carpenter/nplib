# -*- coding: utf-8 -*-

import os

from . import builtins

__all__ = [builtins]

# some global variables
# I think the two SHELL_STATUS variables should be consolidated into one
SHELL_STATUS_RUN = 1
SHELL_STATUS_STOP = 0
HISTORY_PATH = os.path.expanduser('~') + os.sep + '.npshell_history'
