# The code will return the sum of a list except the min value

var = [1, 2, 3, 4, 5, -1]

def sum_without_smallest(a: list):
    a.pop(a.index(min(a)))
    print(a)
    return sum(a)

print(sum_without_smallest(var))