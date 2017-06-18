#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests


class Scout(object):
    def __init__(self):
        self.scouting = False

    def scout(self):
        pass


class Hunter(object):
    def __init__(self):
        self.hunting = False

    def hunt(self):
        pass


def main():
    r = requests.get('https://www.python.org')
    print r


# Execute as a script
if __name__ == '__main__':
    main()
