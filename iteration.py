# -*- coding: utf-8 -*-
import os
from Canvas import Line
a = os.listdir("d:\\TMP")
print a
with open("d:\\TMP\\isup.log") as f:
    try:
        while True:
            line = next(f)
            print line
    except StopIteration:
        pass

liter = [1,2,3,"abc", 'cde', 'efr']
itermList = iter(liter)
while True:
    iterm = next(itermList, None)
    if None == iterm:
        break
    print iterm    
    


def frange(start, end, step):
    x =  start
    while x < end:
        yield x
        x += step

a = list(frange(1, 5, 2))
print a

for item in frange(1, 10, 1):
    print item
    
    
def countdown(n):
    print "start counting......"
    while n > 0:
        yield n
        n -= 1
c = countdown(5)
print "start to print"
print next(c)
print next(c)
print next(c)
print next(c)
print next(c)
'''start to print
start counting......
5
4
3
2
1'''


class CountDown(object):
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        tmp = self.start
        while tmp > 0:
            yield tmp
            tmp -= 1
    def __reversed__(self):
        tmp = 1;
        while tmp < self.start:
            yield tmp;
            tmp += 1
print 'test countdown:'
cd = CountDown(5)
for item in cd:
    print item
    
for item in reversed(cd):
    print item


date=[1,2,3,4,5,6,7]
datelist = list(enumerate(date, 5))
print datelist


print "--------------zip---------------------"
aList = ['a', 'b', 'c']
bList = ['t', 'y', 'u', 'q']
c = zip(aList, bList)
print c

print "--------------- itertool ---------------"
items = ["a", 'b', 'c']
from itertools import permutations
for item in permutations(items):
    print item
for item in permutations(items, 2):
    print item
    
from itertools import combinations
for item in combinations(items, 3):
    print item
for item in combinations(items, 2):
    print item


print "___________ enumerate________________"
items = ["a", 'b', 'c']
for idx, item in enumerate(items):
    print idx, item
print "..................."
for idx, item in enumerate(items, start=5):
    print idx, item
    
    
print "------------------chain-------------------"
from itertools import chain
print aList
print bList
c = chain(aList, bList)
print c
for item in c:
    print item   
    
    
print "----------------- with-----------------"
with open("d:\\TMP\\test.txt", "rt") as f:
    for line in f:
        print line
        
print "-------------------print-------------------"
print (1,2,3,4,6)


print "----------------os---------------------------"
fileTest = "d:\\TMP\\test.txt"
print os.path.basename("d:\\TMP\\test.txt")
print os.path.dirname("d:\\TMP\\test.txt")
print os.path.join("d:\\", "TMP", "test.txt")

print os.path.isfile("d:\\TMP\\test.txt")
print os.path.isfile("d:\\")

print os.path.isdir("d:\\")
print os.path.isdir("d:\\TMP\\test.txt")

print os.path.getsize(fileTest)
mTime = os.path.getmtime(fileTest)

import time
print time.ctime(mTime)

#�б�Ŀ¼�������ļ��� Ŀ¼������Ŀ¼�����е�python�ļ�

dir = "d:\\TMP"
fileList = [name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))]
print fileList

dirList = [name for name in os.listdir(dir) if os.path.isdir(os.path.join(dir, name))]
print dirList

pyList = [name for name in os.listdir(dir) if name.endswith(".py")]
print pyList

import fnmatch
ueList = [name for name in os.listdir(dir) if name.startswith("ue")]
print ueList

import os
import glob
pyfiles = glob.glob("*.py")
for pyfile in pyfiles:
    filesize = os.path.getsize(pyfile)
    filemtime = os.path.getmtime(pyfile)
    print time.ctime(filemtime)
    print filesize, filemtime
    print os.stat(pyfile)
    

from tempfile import TemporaryFile
with TemporaryFile("w+t", dir="d:\\TMP") as f:
    print f.name
    f.write("hello")
    f.seek(0)
    print f.read()
    tmpList = os.listdir("d:\\TMP")
print [name for name in tmpList if name not in os.listdir("d:\\TMP")]

import pickle
print aList


print bList
f = open("d:\\TMP\\test.txt", "w")
pickle.dump(aList, f)
f.close()
f = open("d:\\TMP\\test.txt", "r")
pList = pickle.load(f)
print pList
f.close()


#parameters
def printmeters(first, *rest):
    for item in rest:
        print item
    return (first + sum(rest))/(1 + len(rest))
print printmeters(1)
print printmeters(1,2,3,4,5,6)

def dicparameter(first, **dic):
    for item in dic.items():
        print item
    for item in dic.keys():
        print item
    for item in dic.values():
        print item
dicparameter(3, abc="23", bc="34")

