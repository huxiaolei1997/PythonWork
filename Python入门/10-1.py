# -*- coding: utf-8 -*-
# 下面用循环生成一个 x*x 数组
L = []
for x in range(1,11):
    L.append(x * x)
print (L)
# 下面用一个列表生成式来生成一个 x*x 数组
L2 = [x * x for x in range(1, 11)]
print (L2)