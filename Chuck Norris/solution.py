import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

message = input()

message_bin = []

for i in message:
    word = (bin(ord(i))[2:])
    message_bin.append(word.rjust(7, '0'))

msjbin = ''.join(message_bin)

lastChar = None
output = ''

for c in msjbin:
    if lastChar == c:
        output += '0'
        continue

    if output != '':
        output += ' '

    lastChar = c
    output += '0 0' if c == '1' else '00 0'

print(output)

