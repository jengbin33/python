# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import random
card = []
shape = ['s','h','d','c']
number = ['a','2','3','4','5','6','7','8','9','10','j','q','k']
score  =  {'a': 1,'2': 2,'3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
           '9': 9, '10': 10, 'j': 10, 'q': 10, 'k': 10}
for i in shape:
    for n in number:
        card.append(i+n)
print(card)
for i in range(50):
    
    ran = random.randint(0, 51)
    val = card.pop(ran)
    card.insert(0, val)
print(card)
player = 7
holds = []
for i in range(player):
    holds.append([])
for a in range(0,3):
    for i in range(player):
        holds[i].append(card[0])
        card.pop(0)
print(holds)
p = 0
winner = 0
winner_score = 0
for i in holds:
    sum = 0
    p += 1
    print (i)
    for c in i:
        sum += score[c[1:]]
    print(sum)
    if sum > 21:
        continue
    if sum > winner_score:
        winner = p
        winner_score = sum
print(winner, winner_score)