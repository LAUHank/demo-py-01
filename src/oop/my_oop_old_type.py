#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Dad :
    def __init__(self, name='', car=0, money=0.0) :
        self.name = name
        self.car = car
        self.money = money

    def drive(self) :
        print '老子开车上高速'

    def buy(self) :
        print '%s_%s_%s' % ('老子有', self.money, 'RMB')

    def __repr__(self) :
        return str((self.name, self.car, self.money)) + '_repr'

    def __str__(self) :
        return str((self.name, self.car, self.money))

class Son(Dad) :
    pass

class FirstSon(Dad) :
    def drive(self) :
        print '大儿子开车上高速'

class SecondSon(Dad) :
    def __init__(self, tank='', name='', car=0, money=0.0) :
        Dad.__init__(self)
        self.tank = tank
        self.name = name
        self.car = car
        self.money = money

    def driveTank(self) :
        print '开坦克_' + str(self.tank)

def test() :
    d = Dad(name='lhl')
    d = Son(name='James', car=23, money=1000.0) 
    d = FirstSon(name='Jack', car=2, money=199.0)
    d = SecondSon(tank='M60', name='Bush', car=3, money=99.0)
    testDad(d)

def testDad(d) :
    print d
    print str(d)
    print repr(d)
    print '================'
    print d.name
    d.drive()
    d.buy()
    if isinstance(d, SecondSon) :
        print d.tank
        d.driveTank()

if __name__ == '__main__' :
    test()
