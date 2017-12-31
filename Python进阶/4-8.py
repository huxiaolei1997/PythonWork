# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name, score):
        self.naem = name
        self.__score = score

    def get_grade(self):
        if self.__score >= 90:
            return 'A-优秀'
        elif self.__score >= 60:
            return 'B-及格'
        else:
            return 'C-不及格'

p1 = Person('Bob', 90)
p2 = Person('Alice', 65)
p3 = Person('Tim', 48)

print(p1.get_grade())
print(p2.get_grade())
print(p3.get_grade())

# Person类中有一个私有属性__score， 同时有一个实例方法可以访问到这个__score属性，并返回相应的
# 成绩等级
# A-优秀
# B-及格
# C-不及格

# 在实例方法内部，可以访问所有实例属性，
# 这样，如果外部需要访问私有属性，
# 可以通过方法调用获得，这种数据封装的形式除了能保护内部数据一致性外，
# 还可以简化外部调用的难度。

