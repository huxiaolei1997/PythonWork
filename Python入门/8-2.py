# -*- coding:utf-8 -*-
L = range(1, 101)
print (L[-10:])
print (L[-46::5])
#还有一种写法，切片的嵌套
print (L[4::5][-10:])
#执行结果是
#range(91, 101)
#range(55, 101, 5)，不包括101
#range(55, 105, 5)，不包括105