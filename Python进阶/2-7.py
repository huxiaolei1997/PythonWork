# -*- coding: utf-8 -*-

print (sorted(['bob', 'about', 'Zoo', 'Credit'],key=str.upper,reverse=True))
# 以上是python3.x以上的写法，reverse可省略不写，默认False， True表示逆向排序
# key接受一个函数，这个函数只接受一个元素，默认为None
# reverse是一个布尔值。如果设置为True，列表元素将被倒序排列，默认为False
