# -*- coding: utf-8 -*-
# 下面的代码实现了求积函数

from functools import  reduce
def prod(x, y):
    return x * y
print (reduce(prod, [2, 4, 5, 7, 12]))

# 这里需要注意的是，在python3.x以上的版本中，reduce已经从全局名字空间里面移除了
# 要使用的话就必须先引入 from functools import reduce
# reduce()还可以接收第3个可选参数，作为计算的初始值。具体例子看下面的代码，
# 下面的代码实现了一个求和函数，可以看到运行结果分别是30， 130
# 一个传入了第3个参数，另一个没有传入第3个参数

def sum1(x, y):
    return x + y
print (reduce(sum1, [2, 4, 5, 7, 12]))
print (reduce(sum1, [2, 4, 5, 7, 12], 100))
