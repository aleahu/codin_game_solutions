import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
z = {}
poz = ''
helper = []
n = int(input())  # the number of temperatures to analyse
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    if t > 0:
        z.update({t: [i for i in range(t)]})
        helper = [(key, len(z[key])) for key in z.keys()]
    elif t < 0:
        poz = t - t - t
        z.update({t: [i for i in range(poz)]})
        helper = [(key, len(z[key])) for key in z.keys()]
    elif t == 0:
        z.update({t: t})
        helper.append((t, t))

if not helper:
    print('0')
else:
    helper.sort(key=lambda x: x[1])
    if helper[0] == 0:
        print(helper[0][0])
    elif len(helper) == 1:
        print(helper[0][0])
    elif helper[0][1] == helper[1][1] and helper[0][0] < 0:
        print(helper[1][0])
    else:
        print(helper[0][0])
