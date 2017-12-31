# -*- coding: utf-8 -*-
class Person(object):
# Python pass是空语句，是为了保持程序结构的完整性
# pass 不做任何事情，一般用做占位语句
    pass
p1 = Person()
p1.name = 'Bart'

p2 = Person()
p2.name = 'Adam'

p3 = Person()
p3.name = 'Lisa'

L1 = [p1, p2, p3]
# 用sorted排序
L2 = sorted(L1, key = lambda x : x.name, reverse=True)

print(L2[0].name)
print(L2[1].name)
print(L2[2].name)