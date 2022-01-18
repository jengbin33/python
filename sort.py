# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 21:19:31 2021

@author: jengbin
"""

a = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S",\
     "T","U","V","W","X","Y","Z","a","b","c","d","e","f","g","h","i","j","k","l",\
     "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
def mysort():
    for i in range(len(a)-1,1,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    print(a) 

def search(x):
    left = 0
    right = len(a)-1
    while left <= right:
        middle = (left + right) // 2
        if a[middle] > x:
            right = middle - 1
        elif a[middle] < x:
            left = middle + 1
        else:
            return middle
    return None
def enc(key, sen):
    b = ""
    for i in sen:
        c = search(i)
        if c is not None:
            c += key
            if c >= len(a):
                c -= len(a)
            b += a[c]
        else:
            b += i
    return b
def dec(key, sen):
    b = ""
    for i in sen:
        c = search(i)
        if c is not None:
            c -= key
            b += a[c]
        else:
            b += i
    return b
def breakENC(sen):
    import nltk
    nltk.download('words')
    from nltk.corpus import words 
    for i in range(1,52,1):
        found = True
        e = dec(i, sen)
        f = e.split()
        print(f)
        for j in f:
            if not j in words.words():
                found = False
                break
        if found == True:
            return i
sen = "I went the park yesterday"
d = enc(5, sen)
print(d)
e = dec(5, d)
print(e)
breakENC(d)
















