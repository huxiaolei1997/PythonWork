# -*- coding:utf-8 -*-
def greet(word = 'world'):
    print ('Hello, %s.' %word)
greet()
greet('世界')
#如果给这个greet函数传入了值，那么就打印出Hello,相应的值，
#如果没有给这个greet函数传入值，那么就打印出Hello,world.