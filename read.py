# -*- coding: utf-8 -*-
"""
Created on Tue Aug 10 08:44:51 2021

@author: jengbin
"""
def main(p, n):
    words = {}
    f = open(p+'\\'+n,'r',encoding='utf-8')
    book = f.read()
    book = book.lower()
    lines = book.split('\n')    
    print(lines[0])
    print(len(lines))
    for i in lines:
        i = str(i.encode("ascii","ignore"))
        if len(i)>0:
            w = i.split(' ')
            for a in w:
                if a in words.keys():     
                    words[a]+=1
                else:
                    words[a] = 1
    f.close()
    b = sorted(words, key = words.get, reverse = True)
    count = 0
    for key in b:
        print(key,words[key])
        count += 1
        if count > 10:
            break
if __name__ == '__main__':
    path = 'C:\\Users\\jengbin\\Downloads'
    name = 'Tom.txt'
    main(path, name)
    