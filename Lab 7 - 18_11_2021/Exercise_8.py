# The code will return the nearest local max values in a list
# The code do not implement any kind of input-control, so make sure to type at least two maxes

var = []
maxes = []
maxes_indexes = []
maxes_distances = []

n = input("Type n... ")

while n != " ":
    var.append(float(n))
    n = input("Type n... ")

for i in range(1, len(var) - 1, 1):
    if var[i-1] <= var[i] and var[i+1] <= var[i]:
        maxes.append(var[i])

for i in range(len(maxes) - 1):
    maxes_distances.append(abs(var.index(maxes[i]) - abs(var.index(maxes[i + 1]))) - 1)

nearest_maxes_couple = (maxes[maxes_distances.index(min(maxes_distances))], maxes[maxes_distances.index(min(maxes_distances)) + 1])

print("var: ", var)
print("maxes: ", maxes)
print("distance: ", maxes_distances)
print("nearest maxes (first couple wins): ", nearest_maxes_couple)