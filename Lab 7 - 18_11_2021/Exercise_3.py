# The code will compare two string

var_1 = [1, 2]
var_2 = [1, 1, 2, 2]

def sameSet(a: list, b: list):
    a.sort()
    b.sort()

    for i in range(len(a) - 1):
        if a[i] ==  a[i+1]:
            a.pop(i)
            b.insert(i, 0)

    for i in range(len(b) - 1):
        if b[i] ==  b[i+1]:
            b.pop(i)
            b.insert(i, 0)

    if sum(a) == sum(b):
        return True
    else:
        return False

print(sameSet(var_1, var_2))      
    