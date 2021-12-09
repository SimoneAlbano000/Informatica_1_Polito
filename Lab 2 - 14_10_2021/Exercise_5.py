# The code will do some math on a rectangle, with a, b being the rectangle's sides

from math import sqrt

CONST_a = 3
CONST_b = 4

print("Area: " + str(CONST_a*CONST_b))
print("Perimeter: " + str((CONST_a+CONST_b)*2))
print("Diagonal: " + str(sqrt((CONST_a**2)+(CONST_b**2))))