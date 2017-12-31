# -*- coding: utf-8 -*-
class Person(object):
    __count = 0
    count2 = 0
    @classmethod
    def how_many(cls): # 类方法
        return cls.__count, cls.count2
    def __init__(self, name): # 实例方法
        self.name = name

print(Person.how_many())
p1 = Person('Bob')
print(Person.how_many())

# 通过一个标记一个@classmethod， 该方法将绑定到Person类上，而非类的实例
# 。 类方法的第一个参数将传入类本身，通常将参数名命名为cls，上面的cls.count实际上相当于Person.count
# 因为是在类上调用，而非实例上调用，因此类方法无法获得任何实例变量，只能获得类的引用。