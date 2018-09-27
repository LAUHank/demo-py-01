#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
for line in sys.stdin :
    word_arr = line.strip().split(' ')
    for word in word_arr :
        if word :
            print '%s\t%s' % (word, 1)
