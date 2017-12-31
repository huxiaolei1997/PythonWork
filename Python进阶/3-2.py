# -*- coding: utf-8 -*-

import os.path

# 判断此目录是否存在，打印出True 或者 False
print(os.path.isdir(r'C:\Windows'))
# 判断该目录下的文件是否存在
print(os.path.isfile(r'C:\Windows\notepad.exe'))

# 以上的导入方式是导入了整个模块，如果我们只想导入os.path里面的isdir()和isfile函数
# 我们可以这样写
# from os.path import isdir, isfile
# 如果我们这样导入了函数，那么在调用函数的时候，就不用在函数前面加上包名、模块名

# from os.path import isdir, isfile
# 判断此目录是否存在，打印出True 或者 False
# print(os.path.isdir(r'C:\Windows'))
# 判断该目录下的文件是否存在
# print(os.path.isfile(r'C:\Windows\notepad.exe'))

# 除了以上这些，还有这个是需要我们注意的，比如在math模块中有一个log函数，logging
# 模块也有一个log函数，如果同时使用，该怎么解决名字冲突呢？
# 其实如果我们通过import导入模块名，由于必须通过模块名引用函数名，因此不存在冲突

# import math. logging
# print(math.log(10)) # 调用的是math中的log函数
# logging.log(10, 'something') # 调用的是logging中的函数

# 那么如果我们不想导入整个模块，用from...import来导入这个log函数，这个时候，就必然会冲突
# 我们可以通过给其中的log函数起一个别名来避免冲突

# from math import log
# from logging import log as logger
# print(log(10)) # 调用的是math中的log函数
# logger(10, 'import from logging') # 调用的是logging中的log函数
