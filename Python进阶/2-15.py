# -*- coding: utf-8 -*-
import functools

sorted_ignore_case = functools.partial(sorted, key = str.lower)

print(sorted_ignore_case(['bob', 'about', 'Zoo', 'Credit']))

# python中的偏函数，当一个函数有很多参数的时候，调用者就需要提供多个参数。如果减少参数个数，
# 就可以简化调用者的负担。比如， int() 函数可以把字符串转换为整数， 当仅传入字符串时， int()
# 函数默认按十进制转换：
# 但 int() 函数还提供额外的base参数，默认值为10，也就是默认为十进制。如果传入base参数，就可以做N
# 进制的转换
# 比如下面这样
# int('12345', base=8)
# 5349
# int('12345', 16)
# 74565
# 但是这里如果我们要转换大量的二进制字符串，每次都传入int(x, base=2)会非常麻烦，
# 于是，我们想到，可以定义一个 int2() 函数，默认把base=2 传进去：
# def int2(x, base=2):
# return int(x, base)
# 这样一来的话，我们转换二进制就非常方便了，只需要传入一个参数，
# int2('1000000')
# 64
# int2('1010101')
# 85
# functools.partial就是帮助我们创建一个偏函数的，不需要我们自己定义 int2()，可以直接使用下面
# 的代码创建一个新的函数 int2 :
# import functools
# int2 = functools.partial(int, base2)
# int2('1000000')
# 64
# int2('1010101')
# 85
