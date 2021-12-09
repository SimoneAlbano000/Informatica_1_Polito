# The code will calculate pseudo-random number

CONST_a = 32310901
CONST_b = 1729
CONST_m = 2E24
iterations = 100

seed = int(input("Type an integer number as a seed... "))

for i in range(int(iterations)):
    new_val = ((CONST_a*seed)+CONST_b)%CONST_m
    seed = new_val
    print(new_val)
    