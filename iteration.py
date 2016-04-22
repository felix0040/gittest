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







