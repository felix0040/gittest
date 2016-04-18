# -*- coding: utf-8 -*-
'''
MySet is class for set object
'''

class MySet(object):
    def __init__(self, initSet=[]):
        #内部保存数据，删除可能的重复
        self.interSet =[]
        for item in initSet:
            if item not in self.interSet:
                self.interSet.append(item)
        
    def display(self):
        printStr = "{"
        for item in self.interSet:
            printStr += (str(item))
            printStr += ","
        #消除最后的逗号
        if len(self.interSet) > 0:
            printStr = printStr[0:-1]
        printStr += "}"
        print printStr
    
    #是否包含数据    
    def has(self, item):
        if item in self.interSet:
            return True
        return False
    #判断空
    def empty(self):
        if len(self.interSet) == 0:
            return True
        return False
    
    #交集
    def intersect(self, myset2):
        list = []
        for item in self.interSet:
            if myset2.has(item):
                list.append(item)
        tmpObj = MySet(list)
        return tmpObj
    #并集
    def union(self, myset3):
        
        list1 = list(self.interSet)
        list3 = myset3.interSet
        
        for item in list3:
            if item not in self.interSet:
                list1.append(item)
        tmpObj = MySet(list1)
        return tmpObj
    #差集
    def diff(self, diffset):
        list = []
        for item in self.interSet:
            if not diffset.has(item):
                list.append(item)
        tmpObj = MySet(list)
        return tmpObj
    
    #相等
    def equal(self, equalset):
        tmp1 = self.diff(equalset)
        tmp2 = equalset.diff(self)
        if tmp1.empty() and tmp2.empty():
            return True
        return False
        
    #子集
    def propersubset(self, subSet):
        if not(len(subSet.interSet) < len(self.interSet)):
            return False
        for item in subSet.interSet:
            if item not in self.interSet:
                return False
        return True
    
    #包含
    def subset(self, subSet):
        for item in subSet.interSet:
            if item not in self.interSet:
                return False
        return True
    

#测试部分
print "-----------------display------------------"
a = []
myset1 = MySet(a)
myset1.display()
a = [2,3,4,5,6,7]
myset2 = MySet(a)
myset2.display()
a = [3,4,7,8]
myset3 = MySet(a)
myset3.display()
a = [8,9]
myset4 = MySet(a)
myset4.display()
myset5 = MySet([2,3,4,5,6,7])
myset5.display()
myset6 = MySet([4,5,6])
myset6.display()
print "-----------------intersect------------------------"
mytest1 = myset2.intersect(myset1)
mytest1.display()
mytest1 = myset4.intersect(myset2)
mytest1.display()
mytest1 = myset4.intersect(myset3)
mytest1.display()
mytest1 = myset3.intersect(myset2)
mytest1.display()

print "--------------------union---------------------"
mytest2 = myset2.union(myset1)
mytest2.display()
mytest2 = myset2.union(myset3)
mytest2.display()
mytest2 = myset4.union(myset2)
mytest2.display()


print "------------------diff-----------------------"
mytest3 = myset1.diff(myset2)
mytest3.display()
mytest3 = myset2.diff(myset1)
mytest3.display()
mytest3 = myset2.diff(myset3)
mytest3.display()
mytest3 = myset4.diff(myset2)
mytest3.display()

print "------------------equal-------------------------------"
mytest4 = myset1.equal(myset2)
print mytest4
mytest4 = myset2.equal(myset1)
print mytest4
mytest4 = myset2.equal(mytest3)
print mytest4
mytest4 = myset5.equal(myset2)
print mytest4


print "--------------------propersubset-----------------------"
mytest5 = myset1.propersubset(myset2)
print mytest5
mytest5 = myset2.propersubset(myset1)
print mytest5
mytest5 = myset2.propersubset(myset6)
print mytest5
mytest5 = myset5.propersubset(myset2)
print mytest5

print "--------------------subset-----------------------"
mytest5 = myset1.subset(myset2)
print mytest5
mytest5 = myset2.subset(myset1)
print mytest5
mytest5 = myset2.subset(myset6)
print mytest5
mytest5 = myset5.subset(myset2)
print mytest5

print "------------------------has---------------------"
mytest6 = myset1.has(3)
print mytest6
mytest6 = myset2.has(5)
print mytest6
mytest6 = myset2.has(9)
print mytest6