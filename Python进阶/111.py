# -*- coding: utf-8 -*-
def log3(parameter):
    def fn(f):
        def fn2(*args, **kwargs):
            print('call in %s %s' %(f.__name__,parameter))
            return f(*args, **kwargs)
        return fn2
    return fn

@log3('111')
def show4():
    print('show4')
show4()

