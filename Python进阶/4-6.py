# -*- coding: utf-8 -*-
class Person(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Person.count += 1
p1 = Person('Alice')
# 这里的p1对象中没有count属性，所以获取的绑定在Person上的属性值，p2, p3同理
print(p1.count)
print(Person.count)

p2 = Person('Bob')
print(p2.count)
print(Person.count)

p3 = Person('Tim')
print(p3.count)
print(Person.count)


# 以上代码实现了每创建一个对象，count的值就加1，实现了统计创建对象的个数。
# 值得注意的是，每创建一个对象，就调用一次__init__()函数，正是因为这个原因，
# 我们才能统计创建对象的个数
# 这里的count是类的一个属性，是绑定在类上的，同时所有的实例都可以访问这个属性，
# 绑定在实例上的属性，各个实例之间的属性是不会相互影响的，但是绑定在类上的属性
# 每个实例都可以调用它(不能修改，只能调用)