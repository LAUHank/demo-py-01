#!/usr/bin/env python
#-*- coding: utf-8 -*-

def jiao_ji(list1, list2) :
    lst = []
    size = len(list1)
    big_list = list1
    small_list = list2
    if size < len(list2) :
        big_list = list2
        small_list = list1
    for e in big_list :
        if e in small_list :
            lst.append(e)
    return lst

def cha_ji(list1, list2) :
    lst = []
    for e in list1 :
        if e not in list2 :
            lst.append(e)
    return lst

def bing_ji(list1, list2) :
    lst = jiao_ji(list1, list2)
    lst.extend(cha_ji(list1, list2))
    lst.extend(cha_ji(list2, list1))
    return lst

def word_count(lst) :
    mymap = {}
    for e in lst :
        if e in mymap :
            mymap[e] = mymap[e] + 1
        else :
            mymap[e] = 1
    return mymap

def test() :
    lst = ["one","two","three","four","one","two"]
    myset = set(lst)
    for e in myset :
        print e
    print '=================='
    mymap = word_count(lst)
    for kv in mymap.iteritems() :
        # print kv
        print str(kv[0]) +'='+ str(kv[1])
    print '=================='

def test1() :
    # list1 = ["two","three","four"]
    # list2 = ["one","two","three","five","six","seven"]
    list1 = [1, 2, 3]
    list2 = [1, 2, 4]
    lst = jiao_ji(list1, list2)
    for e in lst :
        print e

def main() :
    test()
    print 'hello 我的 world'

if __name__ == '__main__':
    main()
