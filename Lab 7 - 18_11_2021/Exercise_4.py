# This is a dumb exercise

from random import *

TOP = 20
var = []

for i in range(TOP):
    var.append(randint(0, 100))

print(var)
sorted_var = list(var)
sorted_var.sort()
print(sorted_var)
print(var)
