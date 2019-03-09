import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
hpn = []
for i in range(n):
    pi = int(input())
    hpn.append(pi)
hpn = sorted(hpn)

print(min([hpn[i+1] - hpn[i] for i in range(len(hpn)-1)]))


