#!/usr/bin/python
# -*- coding: utf-8 -*-

from lib import to_hex

import codecs
import sys

encoding = sys.argv[0]
filename = encoding + '.txt'

text = u'pi: π'

encoded = text.encode('utf-8')
decoded = encoded.decode('utf-8')

print 'Raw   :', repr(text)
print 'UTF-8 :', to_hex(text.encode('utf-8'), 1)
print 'UTF-16:', to_hex(text.encode('utf-16'), 2)

print 'Original :', repr(text)
print 'Encoded  :', to_hex(encoded, 1), type(encoded)
print 'Decoded  :', repr(decoded), type(decoded)


print 'Writing to', filename
with codecs.open(filename, mode='wt', encoding=encoding) as f:
    f.write(u'pi: \u03c0')

# Determine the byte grouping to use for to_hex()
nbytes = {'utf-8': 1,
          'utf-16': 2,
          'utf-32': 4,
          }.get(encoding, 1)

# Show the raw bytes in the file
print 'File contents:'
with open(filename, mode='rt') as f:
    print to_hex(f.read(), nbytes)


def main():
    pass


# Execute as a script
if __name__ == '__main__':
    main()
