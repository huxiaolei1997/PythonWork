# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name, gender, birth, job):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.job = job
xiaoming = Person('Xiaoming', 'Male', '1990-1-1', job = 'Student')
print(xiaoming.name,xiaoming.job)


# 以上代码定义了一个Person类，然后为Person类添加了一个特殊的__init__()方法，当创建实例时，
# __init__方法被自动调用，我们就能在此为每个实例都统一加上name, gender, birth, job属性
# __init__方法的第一个参数必须是self（也可以用别的名字，但建议使用习惯用法）， 后续参数则可以自由指定，和
# 定义函数没有任何区别，相应地，创建实例的时候，就必须要提供除self以外的参数


