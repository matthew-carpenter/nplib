# -*- coding: utf-8 -*-

import os
import jedi


def cd(args):
    os.chdir(args[0])
    return jedi.SHELL_STATUS_RUN
