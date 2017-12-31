# -*- coding: utf-8 -*-
import types
def fn_get_grade(self):
    if self.score >= 80:
        return 'A'
    if self.score >= 60:
        return 'B'
    return 'C'

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.get_grade = lambda : 'A'


p1 = Person('Bob', 90)
p1.get_grade2 = types.MethodType(fn_get_grade, p1)
print(p1.get_grade2())
print(p1.get_grade) # 是一个函数对象
print(p1.get_grade()) # 调用get_grade()方法

# lambda : 'A' 等价于 return 'A'，相当于一个函数f, 那么f() = 'A'
# 因此，p1.get_grade 相当于p1.get_grade = f, p1.get_grade() = f()
# p1.get_grade是属性， 只不过这里的属性是一个函数对象，
# p1.get_grade()是方法，前面的p1就是调用这个方法的对象，即实例
# 给一个实例动态添加方法并不常见，直接在class中定义要更直观