#!/usr/bin/env python
import sys

count = 0
cur_key = None

for line in sys.stdin:
    key, value = line.split()
    if key == cur_key:
        count += int(value)
    else:
        if cur_key:
            print('%s\t%s' % (cur_key, count))
        cur_key = key
        count = int(value)

print('%s\t%s' %(cur_key, count))
