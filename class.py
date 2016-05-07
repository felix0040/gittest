# -*- coding: utf-8 -*-

class test(object):
    def __init__(self,x, y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        print self.x, self.y
    
    def __str__(self, *args, **kwargs):
        return "x is {0}, y is {1}".format(self.x, self.y)
    
    def __enter__(self):
        print "enter"
    
    def __exit__(self, exc_ty, exc_val, tb):
        print "exit"
    
a = test(3,4)
print a


#format:
_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)
test= Date(2016, 7, 14)
print format(test, "ymd")


#with and class
with a as f:
    print "testing........"
