#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip().split('\t')
    #Filter on date
    if (line[0][0:7] == '2001-11') and (int(line[0][8:10]) >4) and (int(line[0][8:10]) <9):
        #Fitler on from @ernon and not to @enron
        if "@enron" in line[1] and not '@enron' in line[2]: #add "and not"
            print("%s\t1" %line[1])
