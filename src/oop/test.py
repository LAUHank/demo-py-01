#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import oop

def test() :
    stu = oop.Student(name='刘十三',age=25)
    print stu
    gstu = oop.GoodStudent(id=1, name='LAUHank', age=30, salary=1000.23)
    print gstu
    cstu = oop.CStudent()
    print cstu
    badStudent = oop.BadStudent()
    print badStudent

def main() :
    test()
    print 'hw'

if __name__ == '__main__':
    main()
