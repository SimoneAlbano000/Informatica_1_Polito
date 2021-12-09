# The code will calculate the alternate sum of a list of int

var = []

n = input("Type n... ")

while n != " ":
    var.append(int(n))
    n = input("Type n... ")

for i in range(1, len(var), 1):
    if i % 2 != 0:
        var[i] = var[i]*-1

print(var)
print(sum(var))