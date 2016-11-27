"""
Name: Darien Cortez
Email: darien.cortez@gmail.com
Assignment: Homework 2 - Getting your python feet wet
Due: 26 Sep @ 1:00 p.m.
"""

class fraction(object):
    def __init__(self,n=None,d=None):
        self.numerator = n
        self.denominator = d

    def __str__(self):
        return "%s / %s" % (self.numerator , self.denominator)

    def numerator(self,n):
        self.numerator = n 

    def denominator(self,d):
        self.denominator = d

    def __mul__(self,rhs):
        x = self.numerator * rhs.numerator
        y = self.denominator * rhs.denominator
        return fraction(x,y)

    def __add__(self,rhs,n):
        x = self.num*rhs.den + self.den*rhs.num
        y = self.den * rhs.den
        if ((x / y) >= 1)
            n = x / y
            x = x % y
        return Fraction(x,y)

if __name__ == '__main__':
    a = fraction(1,2)
    b = fraction(4,5)
    c = a * b
    print(c)