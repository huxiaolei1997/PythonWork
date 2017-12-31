# -*- coding: utf-8 -*-
class Person(object):
    def __init__(self, name, gender, score):
        self.name = name
        self._gender = gender
        self.__score = score

p = Person('Bob','Male', 59)

print(p.name)
print(p._gender)
print(p.__score)
# print(p._Person__score)

# python对属性权限的控制是通过属性名来实现的，如果一个属性由双下划线开头的(__)，该属性就无法被外部访问。
# 但是并不是完全不能被外部访问了，我们还是能通过p.Person_name来访问这个属性。不能直接通过p.__score访问score，那是
# 因为Python解释器对外把__score变量改成了_Person__score，所以我们可以通过p._Person__score来访问__score变量，但是我们
# 最好不要这么做，因为不同版本的Python解释器可能会把__name改成不同的变量名。总的来说，Python本身没有任何机制阻止你干坏事，一切全靠自觉
# 后注意下面的这种错误写法：
# >>> bart = Student('Bart Simpson', 98)
# >>> bart.get_name()
# 'Bart Simpson'
# >>> bart.__name = 'New Name' # 设置__name变量！
# >>> bart.__name
# 'New Name'
# 表面上看，外部代码“成功”地设置了__name变量，但实际上这个__name变量和class内部的__name变量不是一个变量！内部的__name变量已经被Python解释器自动改成了_Student__name，而外部代码给bart新增了一个__name变量。不信试试：
#
# >>> bart.get_name() # get_name()内部返回self.__name
# 'Bart Simpson'
# _xxx,可以再子类中使用相当于protected ，虽然也可以被外界访问但是按照习惯不应该被访问
#
# __xxx不可以在子类中使用，相当于private，不可以被外界访问，但是python中没有私有化，只是将__xxx转化成了_Classname__xxx，所以访问__xxx会报错，可以访问 '实例对象._Classname__xxx'
#
# __xxx__在python的类中被称为特殊属性，有很多预定义的特殊属性可以使用，但是通常不用于普通属性