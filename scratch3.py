#!/usr/bin/python
# -*- coding: utf-8 -*-

import lib as np


with open('debug.log', 'r') as f:
    src = f.read()
    np.write_file('temp.noc', 'w', src)


def main():
    pass


# Execute as a script
if __name__ == '__main__':
    main()
