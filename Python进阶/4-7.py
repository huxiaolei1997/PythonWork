# -*- coding: utf-8 -*-
class Person(object):
    __count = 0
    gender = 'Male'
    def __init__(self, name):
        self.name = name
        Person.__count += 1
p1 = Person('Bob')
p1.gender = 'FeMale'
print(p1.gender)
p2 = Person('Alice')
print(p2.gender)
# 修改绑定在类上的gender属性值
Person.gender = 'FeMale'
print(Person.gender)
# print(Person.__count)

# 这个__count属性不能被外部访问，是Person类的私有属性，但也不是真正意义上不能被外部访问，
# 可以从上面的代码中看出，Person类绑定了一个gender属性，而对象p1也绑定了一个gender属性
# 这里需要注意的是，这两个gender属性是不同的，千万不要以为这是对绑定在类上的属性重新赋值，而只是给对象p1动态添加了一个gender属性，
# 我们如果要修改类的属性，就必须要在类上修改属性，不能在实例（对象）上修改类的属性，只有p1
# 这个对象有这个gender属性，后面创建的p2是没有这个属性的，p2如果访问这个属性，那么它访问的是
# 类的属性，不是对象p2的属性，所以得到的值是绑定在类上的gender属性的值，