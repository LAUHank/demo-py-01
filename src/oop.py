#!/usr/bin/env python
#-*- coding: utf-8 -*-
__metaclass__ = type
class Person :
    def __init__(self) :
        self.name = 'lhl'
    def getName(self) :
        return self.name
    def setName(self, name) :
        self.name = name
    def greet(self) :
        fmt = '%s says %s'
        ctnt = 'hello world'
        name = self.name
        print fmt % (name, ctnt)
    def eat(self, name = 'person') :
        print name + ' eat food'

class Dad(Person) :
    def __init__(self) :
        super(Dad, self).__init__()

    def eat(self, name = 'dad') :
        print name + ' eat food and meat'

def main() :
    p = Person()
    dad = Dad()
    
    testEat(p, '13')
    testEat(dad, '24')

    testGreet(p)
    testGreet(dad)

def testEat(p = Person(), name = 'nobody') :
    p.eat(name)

def testGreet(p = Person()) :
    p.greet() 

if __name__ == '__main__':
    main()
