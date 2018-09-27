#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
(last_key, count) = (None, 0)
for line in sys.stdin :
    ln = line.strip()
    if ln :
        (key, val) = ln.split('\t')
        if last_key and last_key != key :
            print '%s\t%s' % (last_key, count)
            (last_key, count) = (key, 1)
        else :
            (last_key, count) = (key, count + int(val))
if last_key :
    print '%s\t%s' % (last_key, count)
