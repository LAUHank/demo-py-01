#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
for line in sys.stdin :
    word_arr = line.strip().split('=')
    if len(word_arr) == 2 :
        print '%s\t%s' % (word_arr[0], word_arr[1])
