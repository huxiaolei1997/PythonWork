# -*- coding: utf-8 -*-
import time

def performance(f):
    def fn(*args, **kwargs):
        print(f.__name__ ,'run in',time.time(),'s')
        return f(*args, **kwargs)
    return fn

@performance #使用这个@performance可以避免我们写f = performance(f)这样的代码
def show():
    print('Hello, World!')
show = performance(show)
show()

#下面的代码没有@performance
def show2():
    print('Hello,Python')
hello = performance(show2)
hello()