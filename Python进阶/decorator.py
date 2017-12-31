# -*- coding: utf-8 -*-

import functools

def log(f):
    def fn(x): # 这里只有一个参数x，所以要装饰的函数也必须只有一个参数
        print('call in %s' %(f.__name__))
        return f(x)
    return fn


@log
def show(x):
    print('hello, %s' %x)
show = log(show)
show('x')
test = log(show)
test('xiaolei_hu')

# 下面的例子展示了一个可以接受参数为任意个的函数作为参数
def log2(f):
    def fn2(*args, **kwargs):
        print('这个装饰器可以接受参数为任意个的函数作为参数，call in %s'%f.__name__)
        return f(*args, **kwargs)
    return fn2

@log2
def show2():
    print('show2')
show2 = log2(show2)
show2()

@log2
def show3(a):
    print('show3 %s' %a)
show3 = log2(show3)
show3('a')

# 以上都是不带参数的decorator，下面介绍一种带参数的decorator

def log3(parameter,parameter2):
    def fn(f):
        def fn2(x):
            print('call in %s %s %s' %(f.__name__,parameter,parameter2))
            return f(x)
        return fn2
    return fn

@log3('parameter', 'parameter2')
def show4(a):
    print('show4 %s' %a)
show4('accept two parameters')
print('show4\'s name is %s' %(show4.__name__))

def log3(parameter):
    def fn(f):
        def fn2(*args, **kwargs):
            print('call in %s %s' %(f.__name__, parameter))
            return f(*args, **kwargs)
        fn2.__name__ = f.__name__
        fn2.__doc__ = f.__doc__
        return fn2
    return fn

@log3('parameter')
def show5():
    print('show5')
show5()

@log3('parameter')
def show5(a, b, c):
    print('show5 %s %s %s' %(a, b, c))
show5('one', 'two', 'three')
print('show5\'s name is %s' %show5.__name__)
# 如果这时候我们要打印函数show5()的名字，那么由于使用了decorator，show5()函数的名字将会被改变，实际上，不只是函数名改变了，
# __doc__等其他属性也被改变了，如果要让调用者看不出一个函数经过了decorator的“改造”,就需要把原函数的一些属性复制到新函数中
# 可以从上面看出，没有加
# fn2.__name__ = f.__name__
# fn2.__doc__ = f.__doc__
# 这句代码的decorator，调用的函数的函数名已经被改变了，而加了这句代码的，则函数名和原来的是一样的
# 但是这样写很复杂，有没有一种简单的办法呢？因为我们很难把原函数的所有属性都一个一个复制到新函数上，所以Python内置的
# functools可以用来自动化完成这个“复制”的任务：

def log5(parameter):
    def fn(f):
        @functools.wraps(f)
        def fn2(*args, **kwargs):
            print('call in %s %s' %(f.__name__, parameter))
            return f(*args, **kwargs)
        return fn2
    return fn

@log5('parameter')
def show6():
    print('show6')
show6()

@log5('parameter')
def show6(a, b, c):
    print('show6 %s %s %s' %(a, b, c))
show6('one', 'two', 'three')
print('show6\'s name is %s' %show6.__name__)

# 最后我们可以看到，使用了functools之后，函数名能正常的被获取了
# 还有需要注意的是，由于我们把原函数签名改成了 (*args, **kwargs)， 因此，无法获得原函数的原始参数信息，
# 即便我们采用固定参数来装饰只有一个参数的函数，也可能改变原函数的参数名，因为新函数的参数名始终是

# def log(f):
#      @functools.wraps(f)
#        def wrapper(x):
#           print 'call...'
#            return f(x)
#       return wrapper

# 'x'，原函数定义的参数名不一定叫 'x'