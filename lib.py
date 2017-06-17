#!/usr/bin/python
# -*- coding: utf-8 -*-

import logging

import binascii


def write_file(filename, mode, data):
    with open(filename, mode) as f:
        f.write(data)


def dump_hex(src, hex_bytes=16):
    """Outputs hex values given an input stream.
    """
    dump = []
    # make it unicode aware
    if isinstance(src, unicode):
        digits = 4
    else:
        digits = 2
    # dump it
    for i in xrange(0, len(src), hex_bytes):
        s = src[i:i + hex_bytes]
        offset = b' '.join(["%0*X" % (digits, ord(x)) for x in s])
        ascii = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.' for x in s])
        dump.append(b"%04X %-*s %s" % (i, hex_bytes * (digits + 1), offset, ascii))
    return b'\n'.join(dump)


def init_logging(logmode='console', loglevel='INFO', logfile=None):
    """
    Simplified interface to the logging module.
            logmode: This mode controls how logging is implemented.
                'console':       et the logging level only.
                'append':       Set the logging level and a log file's name in append mode.
                'overwrite':    Set the logging level. Set the log file's name in overwrite mode.
            loglevel: Severity threshold of the messages to report.
                DEBUG	    Detailed information, typically of interest only when diagnosing problems.
                INFO	    General information.
                WARNING     An indication of something unexpected or of a problem in the future (e.g. 'disk space low').
                ERROR	    Due to a more serious problem, the software has not been able to perform some function.
                CRITICAL    A serious error, indicating that the program itself may be unable to continue running.
            filename: Name of the log file to write to.
                Type: String
                Example: 'debug.log'
    """

    def die(msg):
        logging.debug(msg)
        pass

    if logmode == 'console':  # only set the logging threshold (no log file output)
        if loglevel == 'DEBUG':
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
            logging.info(" Logging enabled: %s" % '--verbose')
        elif loglevel == 'INFO':
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)
            logging.info(" Logging enabled: %s" % '--info')
        elif loglevel == 'WARNING':
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.WARNING)
            logging.info(" Logging enabled: %s" % '--warning')
        elif loglevel == 'ERROR':
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.ERROR)
            logging.info(" Logging enabled: %s" % '--error')
        elif loglevel == 'CRITICAL':
            logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.CRITICAL)
            logging.info(" Logging enabled: %s" % '--critical')
        else:
            die("")

    elif logmode == 'append':  # set logging threshold with log file in append mode
        if loglevel == 'DEBUG':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, level=logging.DEBUG)
            logging.info(" Logging enabled: %s" % '--verbose')
        elif loglevel == 'INFO':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, level=logging.INFO)
            logging.info(" Logging enabled: %s" % '--info')
        elif loglevel == 'WARNING':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, level=logging.WARNING)
            logging.info(" Logging enabled: %s" % '--warning')
        elif loglevel == 'ERROR':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, level=logging.ERROR)
            logging.info(" Logging enabled: %s" % '--error')
        elif loglevel == 'CRITICAL':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, level=logging.CRITICAL)
            logging.info(" Logging enabled: %s" % '--critical')
        else:
            die("")

    elif logmode == 'overwrite':  # set logging threshold with log file in overwrite mode
        if loglevel == 'DEBUG':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, filemode='w', level=logging.DEBUG)
            logging.info(" Logging enabled: %s" % '--verbose')
        elif loglevel == 'INFO':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, filemode='w', level=logging.INFO)
            logging.info(" Logging enabled: %s" % '--info')
        elif loglevel == 'WARNING':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, filemode='w', level=logging.WARNING)
            logging.info(" Logging enabled: %s" % '--warning')
        elif loglevel == 'ERROR':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, filemode='w', level=logging.ERROR)
            logging.info(" Logging enabled: %s" % '--error')
        elif loglevel == 'CRITICAL':
            logging.basicConfig(format='%(levelname)s:%(message)s', filename=logfile, filemode='w', level=logging.CRITICAL)
            logging.info(" Logging enabled: %s" % '--critical')
        else:
            die("")

    else:
        die("")


def to_hex(t, nbytes):
    """Format text t as a sequence of nbyte long values separated by spaces.
    """
    chars_per_item = nbytes * 2
    hex_version = binascii.hexlify(t)

    def chunkify():
        for start in xrange(0, len(hex_version), chars_per_item):
            yield hex_version[start:start + chars_per_item]
    return ' '.join(chunkify())
