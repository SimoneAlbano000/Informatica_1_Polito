# The code will translate a num_type grade in an alpha one's

from math import *

alpha = ["A", "B", "C", "D", "F"]

var = float(input("Type the mark in number..."))

if 0 < abs(var - floor(var)) <= 0.3 :
    print(str(alpha[4-int(var)]) + "+")
elif 0.3 < abs(var - floor(var)) <= 0.9 :
    print(str(alpha[3-int(var)]) + "-")
elif abs(var - floor(var)) == 0 :
    print(str(alpha[4-int(var)]))
