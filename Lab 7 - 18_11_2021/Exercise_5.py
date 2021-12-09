# The code will return local max values in a list

var = []
maxes = []

n = input("Type n... ")

while n != " ":
    var.append(int(n))
    n = input("Type n... ")

print(var)

for i in range(1, len(var) - 1, 1):
    if var[i-1] <= var[i] and var[i+1] <= var[i]:
        maxes.append(var[i])

print("Local maxes: ", maxes)
