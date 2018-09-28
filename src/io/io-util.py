#!/usr/bin/env python
#-*- coding: utf-8 -*-
def readFileAsSet(filePath = "myfile") :
    mySet = set()
    try :
        file = open(filePath)
        for line in file :
            mySet.add(line)
    except Exception, e :
        print e
    finally :
        if file :
            file.close()
    return mySet

def readFileAsList(filePath = "myfile") :
    lst = []
    try :
        file = open(filePath)
        for line in file :
            lst.append(line)
    except Exception, e :
        print e
    finally :
        if file :
            file.close()
    return lst

def main() :
    lst = readFileAsList()
    for item in lst :
        print item
    print 'list-done'
    mySet = readFileAsSet('myfile')
    for item in mySet :
        print item
    print 'set-done'

if __name__ == '__main__':
    main()
