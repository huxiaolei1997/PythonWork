# -*- coding : utf-8 -*-

def format_name(s):
    return s.lower()[0].upper() + s.lower()[1:]
print (list(map(format_name, ['adam', 'LISA', 'barT']))) # python3.x版本以上的写法,3.x版本以下去掉list()

# 还有一种可以使用python的内置函数capitalize()

def format_name2(n):
    return n.capitalize()
print (list(map(format_name2, ['adam', 'LISA', 'barT'])))