import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
# ---
# Hint: You can use the debug stream to print initialTX and initialTY, if Thor seems not follow your orders.

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]



# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)
    
    if light_x == initial_tx and light_y < initial_ty:
        print('N')
    elif light_x == initial_tx and light_y > initial_ty:
        print('S')
    elif light_x > initial_tx and light_y < initial_ty:
        print('NE')
    elif light_x > initial_tx and light_y == initial_ty:
        print('E')
    elif light_x > initial_tx and light_y > initial_ty:   # SUD EST pana la diferenta dintre 
        differenceY = light_y - initial_ty
        for i in range(differenceY):
            print("SE")
        differenceX = light_x - differenceY
        for i in range(differenceX):
            print("E")
    elif light_x < initial_tx and light_y > initial_ty:
        differenceY = light_y - initial_ty
        for i in range(differenceY):
            print("SW")
        differenceX = initial_tx - differenceY
        for i in range(differenceX):
            print("W")
        
    elif light_x < initial_tx and light_y == initial_ty:
        print('W')
    else:
        print("NW")
    