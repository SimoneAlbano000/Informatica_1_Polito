# The code will emulate an ATM

CONST_PIN = "1234"
CONST_N = 3

for i in range(CONST_N):
    in_pin = input("Please type the pin... ")
    if in_pin == CONST_PIN:
        print("Pin correct...")
        break
    else:
        print("Pin not correct...")
if i == CONST_N - 1:
    print("You have riched the max number of trials..")
    