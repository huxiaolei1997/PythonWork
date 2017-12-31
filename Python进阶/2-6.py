# -*- coding: utf-8 -*-

import math
def is_sqr(x):
    return math.sqrt(x) == int(math.sqrt(x))

print (list(filter(is_sqr, range(1, 101))))

# 运行结果：[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# filter是python内置的另一个有用的高阶函数
# filter()函数接收一个函数f 和 一个list，这个函数 f 的作用是对每个元素进行判断返回True 或 False,
# filter()根据判断结果自动过滤掉不符合条件的元素，返回符合条件的元素组成的一个新list
# 利用filter()函数还可以完成许多事情，比如删除None或者空字符串或者指定的字符串
# 下面看一个例子

def is_not_empty(s):
    return s and len(s.strip()) > 0
print (list(filter(is_not_empty, ['test', None, '', 'str', ' ', 'END'])))

# 下面的例子实现了删除指定的字符串]
# 需要注意的是在python中，字符串一旦创建了就不能被改变了
# 使用strip()函数也只是返回了一个新的字符串，原来的字符串并没有改变，同时， strip(rm)函数删除的是 s 字符串中开头、结尾处的 rm 序列的字符。
# 且当rm为空时，默认删除空白符（包括'\n', '\r', '\t', ' ')
# 下面看一个例子

a = "123abc"
a.strip("1")
a.strip("c")
print(a)
print(a.strip("1"))
print(a.strip("c"))

# 运行结果
# 123abc
# 23abc