# -*- coding: utf-8 -*-
def calc_prod(lst):
    def calc_prod2():
        sum = 1.0
        for value in lst:
            sum = sum * value
        return sum
    return calc_prod2

f = calc_prod([1, 2, 3, 4])
print (f())