# String classifier

var = input("Type a string...")

if var.isalpha() : 
    print("Alpha ")
    if var.islower() : 
        print("Lowercase ")
    elif var.isupper() : 
        print("Uppercase ")
    elif var[0].isupper() : 
        print("Is Capitalized ")

elif var.isnumeric() : 
    print("All-digit ")

elif var.isalnum() : 
    print("Alpha-num ")
    if var[0].isupper() : 
        print("Is Capitalized ")
