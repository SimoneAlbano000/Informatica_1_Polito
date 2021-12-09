# The code will generate a random list[10] and do stuff

from random import *
TOP = 100

var = []
for i in range(10):
    var.append(randint(1, TOP+1))

print(var)

print("Elements of even index: ", var[::2])

even_var = list(var)
for j in even_var:
    if j%2 != 0:
        even_var.remove(j)

print("Elements of even value: ", even_var)

print("Elements in reverse order: ", var[::-1])

print("First and last element: ", var[0], var[len(var)-1])

