#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import random
import sys

def readFile(filePath = "a.txt", fileMode = "r") :
    try :
        file = open(filePath, fileMode)
        for line in file :
            # print line
            sys.stdout.write(line)
    except Exception, e :
        print e
    finally :
        if file : file.close()
    print "%s_%s_done" % (filePath, fileMode)

def writeFile(filePath = "a.txt", fileMode = "a", ctnt = '写文件测试') :
    try :
        file = open(filePath, fileMode)
        file.write(ctnt)
        file.write(str(random.random()))
        file.write(os.linesep)
    except Exception, e :
        print e
    finally :
        if file : file.close()
    print "%s_%s_done" % (filePath, fileMode)    

def test() :
    # writeFile(filePath='/root/Downloads/io', fileMode='a')
    readFile(filePath='/root/Downloads/io')

if __name__ == '__main__':
    test()
