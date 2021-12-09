# The code will calc taxes

state = input("Type your state (conjugated/non conjugated)...")
isee = int(input("Type your ISEE..."))

if state == "conjugated" :
    if 0 <= isee <= 16000 :
        print("Taxes: ", isee*0.1)
    elif 16000 < isee <= 64000 :
        print("Taxes: ", 1600 + isee*0.15)
    elif isee > 64000 :
        print("Taxes: ", 8800 + isee*0.25)
elif state == "non conjugated" : 
    if 0 <= isee <= 8000 :
        print("Taxes: ", isee*0.1)
    elif 8000 < isee <= 32000 :
        print("Taxes: ", 800 + isee*0.15)
    elif isee > 32000 :
        print("Taxes: ", 4400 + isee*0.25)
else :
    print("Invalid input...")
