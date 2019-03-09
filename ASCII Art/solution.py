import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '?']
chosen_letters = []

for letter in t.lower():
    if letter in alphabet:
        chosen_letters.append(alphabet.index(letter))
    else:
        chosen_letters.append(alphabet.index('?'))

for i in range(h):
    row = input()
    ascii = [ row[i:i+l] for i in range(0, len(row), l) ]
    print(''.join([ascii[i] for i in chosen_letters]))



