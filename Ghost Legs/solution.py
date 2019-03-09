import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

top = []
middle = []
bottom = []

for r in range(h):
    line = input()
    line = line.replace('|-', '> ')
    line = line.replace('-|', ' <')
    if r == 0:
        for v in line:
            if v != ' ':
                top.append(v)
    elif r == h-1:
        for v in line:
            if v != ' ':
                bottom.append(v)
    else:
        line = line.split()
        middle.append(line)
d = {}   
d2 = {}
for index, litera in enumerate(top):
    newindex = index
    for sublista in range(h-2):
        for semn in middle[sublista][newindex]:
            if semn == '|':
                break
            elif semn == '>':
                newindex += 1
                break
            elif semn == '<':
                newindex -= 1
                break
    d.update({litera: newindex})

for index, value in enumerate(bottom):
    d2.update({index:value})

pairs = {}
for key, value in d.items():
    pairs[key] = d2[value]

for key, value in pairs.items():
    print(key+value)