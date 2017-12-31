# -*- coding: utf-8 -*-
def count():
    fs = []
    for i in range(1, 4):
        def f(m = i):
            return m * m
        # 如果这里这样写 fs.append(f())那么这个返回值不是函数，而是一个具体的值
        fs.append(f)
    return fs
f1, f2, f3 = count()
print (f1(), f2(), f3())