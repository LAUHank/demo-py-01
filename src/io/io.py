#!/usr/bin/env python
#-*- coding: utf-8 -*-
import os
import random

def readFile(filePath = "a.txt", fileMode = "r") :
    try :
        file = open(filePath, fileMode)
        for line in file :
            print line
    except Exception, e :
        print e
    finally :
        if file :
            file.close()
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
        if file :
            file.close()
    print "%s_%s_done" % (filePath, fileMode)    

def main() :
    #readFile(filePath = "a.txt", fileMode = "r")
    #readFile(fileMode = "r", filePath = "a.txt")
    writeFile()
    #readFile()

if __name__ == '__main__':
    main()
