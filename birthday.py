# -*- coding: utf-8 -*-
"""
Created on Tue Jan 11 21:27:36 2022

@author: jengbin
"""

import random, datetime

def getBirthdays (number):
    Birthdays = []
    for i in range(number):
        start = datetime.date(2022,1,1)
        days = datetime.timedelta(random.randint(0, 364))
        birthday = start + days
        Birthdays.append(birthday)
    return Birthdays 
print(getBirthdays (10))
def getMatched(birthdays):
    for i in range(0,len(birthdays)-1,1):
        for j in range(i+1,len(birthdays),1):
            if birthdays[i] == birthdays[j]:
                return birthdays[i]
    return None
count = 0
for i in range(10000):
    a = getBirthdays(50)
    b = getMatched(a)
    if b is not None:
        count += 1
print(count)