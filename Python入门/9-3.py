# -*- coding: utf-8 -*-
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }

sum1 = 0.0
for key in d:
    sum1 += d[key]
print (sum1 / len(d))

# 还可以这样实现

scoreList = d.values()
print (sum(scoreList) / len(scoreList))

# 或者还可以这样实现

# sum2 = 0.0
# for score in d.itervalues(): 这个方法在python3.0以上已经被移除了
#     sum2 += score
# print (sum2 / len(d))