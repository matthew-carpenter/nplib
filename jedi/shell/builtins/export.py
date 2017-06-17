# -*- coding: utf-8 -*-

import os
import jedi


def export(args):
    if len(args) > 0:
        var = args[0].split('=', 1)
        os.environ[var[0]] = var[1]
    return jedi.SHELL_STATUS_RUN
