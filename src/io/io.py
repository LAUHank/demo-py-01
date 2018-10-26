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

def writeFile(filePath = "a.txt", fileMode = "a", ctnt = '写文件测试', eol = os.linesep) :
    try :
        file = open(filePath, fileMode)
        file.write(ctnt)
        file.write(str(random.random()))
        file.write(eol)
    except Exception, e :
        print e
    finally :
        if file : file.close()
    print "%s_%s_done" % (filePath, fileMode)    

def test() :
    filePath = 'my_io_file.txt' # '/root/Downloads/io'
    # 无论是读还是写, Python会自动将\n转换成相应OS的换行符
    writeFile(filePath, fileMode='a', eol='\n') 
    # readFile(filePath)

if __name__ == '__main__':
    test()
