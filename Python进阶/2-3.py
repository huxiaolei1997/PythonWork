# -*- coding: utf-8 -*-
import math

def add(x, y, f):
    return f(x) + f(y)

print (add(25, 9, math.sqrt))

# 这里传入了一个math.sqrt作为函数的变量，所以add函数实际执行的代码是abs(25) + abs(9)

# 或者也可以写

def sqrt1(a):
    return math.sqrt(a)

def add2(x, y, f):
    return f(x) + f(y)

print (add2(25, 9, sqrt1))