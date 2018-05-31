# -*- coding: utf-8 -*-
class Person(object):

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

class Student(Person):

    def __init__(self, name, gender, score):
        super(Student, self).__init__(name, gender)
        self.score = score

    def __str__(self):
        return '(Student:%s,%s,%s)' %(self.name, self.gender, self.score)
    __repr__ = __str__
    # __str__()
    # 用于显示给用户，而__repr__()
    # 用于显示给开发人员。
    #
    # 如果在交互式命令行下
    # 直接敲变量
    # s
    # 就会返回 < main.Person object at XXX > 这样的东西
    #
    # 如果你配置了__repr__ = __str__
    #
    # 你交互式命令行下打print
    # s
    # 和
    # 直接敲变量
    # s
    # 的返回值是一样的
    # 都是(Student: Bob, male, 88)
s = Student('Bob', 'male', 88)
print(s)

# 如果要把一个类的实例变成 str，就需要实现特殊方法__str__()：
#
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return '(Person: %s, %s)' % (self.name, self.gender)
# 现在，在交互式命令行下用 print 试试：
#
# >>> p = Person('Bob', 'male')
# >>> print p
# (Person: Bob, male)
# 但是，如果直接敲变量 p：
# >>> p
# <main.Person object at 0x10c941890>
# 似乎__str__() 不会被调用。
#
# 因为 Python 定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。
#
# 有一个偷懒的定义__repr__的方法：
#
# class Person(object):
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#     def __str__(self):
#         return '(Person: %s, %s)' % (self.name, self.gender)
#     __repr__ = __str__