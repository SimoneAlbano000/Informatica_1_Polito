# The code will display n prime numbers that are less then "stop"

stop = int(input("Type the stop value... "))

dividers = []
primes = []

for i in range(2, stop + 1, 1):
    dividers.clear()
    for j in range(2, i + 1, 1):
        if i % j == 0:
            dividers.append(j)
    if dividers[0] == i:
        primes.append(i)
        
print(primes)
