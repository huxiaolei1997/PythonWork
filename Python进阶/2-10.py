# -*- coding: utf-8 -*-
def is_not_empty(s):
    return s and len(s.strip()) > 0
print(list(filter(is_not_empty, ['test', None, '', 'str', ' ', 'END'])))

# 上面的这种写法是直接传入了一个函数is_not_empty，这样看起来很复杂
# 我们可以用匿名函数来简化上面的代码

print (list(filter(lambda s: s and (len(s.strip())) > 0, ['test', None, '', 'str', ' ', 'END'])))

# 可以看到用匿名函数实现了之后，代码简洁了很多
# 这里还有需要注意的是返回函数的时候，也可以返回一个匿名函数
# 下面看一个例子
myabs = lambda x: -x if x < 0 else x
print(myabs(-1))
# 上面的 -x if x < 0 else x表示，这是一种简单的写法
# if < 0
#   -x
# else:
#   x