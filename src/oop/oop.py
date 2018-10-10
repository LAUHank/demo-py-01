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

class Student :
    def __init__(self, id = 0, name = '', age = 0) :
        self.id = id
        self.name = name
        self.age = age
    def __str__(self) :
        result = 'Student {"id" : '+str(self.id)+', "name" : '+self.name+', "age" : '+str(self.age)+'}'
        return result

class CStudent(Student) :
    pass

class BadStudent(Student) :
    def __str__(self) :
        result = 'BadStudent'
        return result

class GoodStudent(Student) :
    def __init__(self, id=0, name='刘十三', age=0, salary=0.0) :
        super(Student, self).__init__()
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

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
