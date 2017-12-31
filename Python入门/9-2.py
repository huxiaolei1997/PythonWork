# -*- coding: utf-8 -*-
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in zip(range(1, len(L) + 1), L):
    print (index, '-', name)
L = ['Adam', 'Lisa', 'Bart', 'Paul']
for index, name in enumerate(L):
    print (index + 1, '-', name)