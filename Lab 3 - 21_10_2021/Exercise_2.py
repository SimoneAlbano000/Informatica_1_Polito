# The code will translate an alpha_type grade in a numerical one's

alpha = ["A", "B", "C", "D", "F"]
num = [4, 3, 2, 1, 0]

var = input("Type the mark in letter with optional sign(+, -)...")

if len(var) == 2 and var != "A+" :
    if var[1] == "+" :
        print(num[alpha.index(var[0])] + 0.3)
    elif var[1] == "-" :
        print(num[alpha.index(var[0])] - 0.3)
else : 
    print(num[alpha.index(var[0])])
