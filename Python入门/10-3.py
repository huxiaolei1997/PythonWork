# -*- coding: utf-8 -*-
def toUppers(L):
    return [x.upper() for x in L if isinstance(x, str)]
print (toUppers(['Hello', 'world', 101]))

# isinstance() 函数来判断一个对象是否是一个已知的类型
# object -- 实例对象。
# classinfo -- 可以是直接或间接类名、基本类型或者有它们组成的元组。