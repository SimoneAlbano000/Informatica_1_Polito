# The code will get rid of errors for all values in a list

var = [1, 2, 3, 4, 5]
lenth = len(var)

var.append(var[0:2])
for iter in range(lenth - 2):
    var.append(var[iter:iter+3])
var.append(var[lenth -2:lenth])

var = var[lenth:len(var)]

for i in range(lenth):
    var[i] = sum(var[i])/len(var[i])

print(var)