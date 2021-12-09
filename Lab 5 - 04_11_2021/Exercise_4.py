# The code will factorize any tiped numbers

from math import floor

number = int(input("Type a number to factorize... "))

def factorize(number):
    for i in range(2, number + 1, 1):
        while number % i == 0:
            number = number/i
            yield i

print(list(factorize(number)))