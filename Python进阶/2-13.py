# -*- coding: utf-8 -*-
import time
def p(unit):
    def performance(f):
        def fn(*args, **kwargs):
            print('call %s %s' %(time.time(),unit))
            return f(*args,**kwargs)
        return fn
    return performance
@p('s')
def show():
    print('hello')
print(show())

# 最外层函数接收参数，下一层函数接收被装饰的函数