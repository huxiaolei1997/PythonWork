# -*- coding: utf-8 -*-
import functools,time
from functools import reduce

def performance(unit):
    def fn(f):
        @functools.wraps(f)
        def fn2(*args, **kw):
            print ('call in %s' %time.time())
            return f(*args, **kw)
        return fn2
    return fn

@performance('ms')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))

print(factorial.__name__)

# 如何实现一个完整的decorator，具体介绍和例子见 2-14