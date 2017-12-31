# -*- coding: utf-8 -*-
class Person(object):
    pass

xiaoming = Person()
xiaohong = Person()

print(xiaoming)
print(xiaohong)
print(xiaoming == xiaohong)

# 上面的代码实现了定义了一个类，并创建了两个类的实例，最后打印出了这两个实例，并比较了这两个实例是否相等
# 按照 Python 的编程习惯，类名以大写字母开头，紧接着是(object)，
# 表示该类是从哪个类继承下来的。类的继承将在后面的章节讲解，现在我们只需要简单地从object类继承。
# 有了Person类的定义，就可以创建出具体的xiaoming、xiaohong等实例。创建实例使用 类名+()，类似函数调用的形式创建：