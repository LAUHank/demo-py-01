#!/usr/bin/env python
#-*- coding:utf-8 -*-

'''module note'''
__metaclass__ = type
class Dad :
# class Dad(object) :
    '''class Dad note'''
    def __init__(self, name='', car=0, money=0.0) :
        self.name = name
        self.car = car
        self.money = money

    def drive(self) :
        '''method drive note'''
        print '老子开车上高速'

    def buy(self) :
        print '%s_%s_%s' % ('老子有', self.money, 'RMB')

    def __repr__(self) :
        return self.__str__() + '_repr'

    def __str__(self) :
        return str((self.name, self.car, self.money))

class Son(Dad) :
    pass

class FirstSon(Dad) :
    def drive(self) :
        print '大儿子开车上高速'

class SecondSon(Dad) :
    def __init__(self, tank='', name='', car=0, money=0.0) :
        super(SecondSon, self).__init__(name, car, money)
        self.tank = tank

    def driveTank(self) :
        print '开坦克_' + str(self.tank)

class ThirdSon(Dad) :
    def __init__(self, tank='', name='', car=0, money=0.0) :
        super(ThirdSon, self).__init__(name, car, money)
        self.tank = tank

    def driveTank(self) :
        super(ThirdSon, self).drive()
        print '3son开坦克_' + str(self.tank)

    def __str__(self) :
        return super(ThirdSon, self).__str__() + ', ' +str(self.tank)

def test() :
    d = Dad(name='lhl')
    d = Son(name='James', car=23, money=1000.0) 
    d = FirstSon(name='Jack', car=2, money=199.0)
    d = SecondSon(tank='M60', name='Bush', car=3, money=99.0)
    d = ThirdSon(tank='M60E3', name='Trump', car=30, money=9.0)
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
    if isinstance(d, ThirdSon) :
        print d.tank
        d.driveTank()

if __name__ == '__main__' :
    test()
