# The code will check if the input number are increasing, decreasing or neither of those

first = int(input("Enter the first number..."))
second = int(input("Enter the second number..."))
third = int(input("Enter the third number..."))

if first < second < third :
    print("Increasing")
elif first > second > third :
    print("Decreasing")
else : 
    print("Neither")
