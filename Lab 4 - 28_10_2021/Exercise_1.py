# The code will do stuff on typed numbers

vals = []
i = 0
n = (input("Inserire un numero n, \" \" per terminare... "))


# Print max & min
while 1:
    if n == " ":
        break
    else:
        vals.insert(i, int(n))
        n = (input("Inserire un numero n, \" \" per terminare... "))
        i = i + 1

print("Max: ", max(vals))
print("Min: ", min(vals))


# Print even & odd numbers of int
even = 0
odd = 0

for j in range(len(vals)):
    if vals[j]%2 == 0:
        even = even + 1
    else :
        odd = odd + 1

print("Even numbers: ", even)
print("Odd numbers: ", odd)


# Print  all the partial sums
sum = 0

for j in range(len(vals)):
    sum = sum + vals[j]
    print(sum)

# Print all the adiacent duplicates
for j in range(len(vals) - 1):
    if vals[j] == vals [j + 1]:
        print(vals[j])

