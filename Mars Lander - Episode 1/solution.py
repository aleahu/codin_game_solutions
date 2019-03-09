import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

surface_n = int(input())  # the number of points used to draw the surface of Mars.
for i in range(surface_n):
    land_x, land_y = [int(j) for j in input().split()]

# game loop
while True:
    # h_speed: the horizontal speed (in m/s), can be negative.
    # v_speed: the vertical speed (in m/s), can be negative.
    # fuel: the quantity of remaining fuel in liters.
    # rotate: the rotation angle in degrees (-90 to 90).
    # power: the thrust power (0 to 4).
    x, y, h_speed, v_speed, fuel, rotate, power = [int(i) for i in input().split()]
    if abs(v_speed) < 20:
        print('0 1')
    elif abs(v_speed) < 30 and abs(v_speed) > 19:
        print('0 2')
    elif abs(v_speed) < 40 and abs(v_speed) > 29:
        print('0 3')
    elif abs(v_speed) > 39:
        print('0 4')
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)   