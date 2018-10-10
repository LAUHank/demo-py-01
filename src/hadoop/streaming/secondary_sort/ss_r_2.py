#!/usr/bin/env python
#-*- coding: utf-8 -*-

import sys

last_key = None
lst = []
for line in sys.stdin :
    ln = line.strip()
    if ln :
        (key, val) = ln.split('\t')
        if last_key and last_key != key :
            lst.reverse()
            for e in lst :
                print '%s\t%s' % (e[0], e[1])
            last_key = key
            lst = []
            lst.append((last_key, val))
        else :
            last_key = key
            lst.append((last_key, val))
if last_key :
    lst.reverse()
    for e in lst :
        print '%s\t%s' % (e[0], e[1])
