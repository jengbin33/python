# -*- coding: utf-8 -*-
"""
Created on Tue Oct 26 20:15:09 2021

@author: jengbin
"""
def multiply(a,b):
    return a*b

def gugudan(f,t):
    if f > t:
        print("error")
        return
    a = f
    while a < t+1 :
        b = 1
        while b < 10:
            print("{} x {} = {}".format(a, b, multiply(a,b)))
            b += 1
        a += 1
gugudan(4,3)
gugudan(7,8)