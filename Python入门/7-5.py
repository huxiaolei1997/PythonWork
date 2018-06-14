# -*- coding:utf-8 -*-
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1 )
print (fact(100))
# 递归调用 fact 方法