# Exercise 7
# The code will increment a variable adding 5% to it 3 times

balance = 1000
print("Balance: ", balance)
for i in range(3):
    balance = (balance*1.05)
    print("Balance, year ", i+1, ":", balance)
