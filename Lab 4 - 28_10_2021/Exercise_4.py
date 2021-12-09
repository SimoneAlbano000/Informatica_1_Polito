# The code will do some string stuff

string = input("Type a string... ")

print("The reversed string is: ", string[::-1])

print("Only uppercase char from the end... ")
for i in string[::-1]:
    if i.isupper():
        print(i)
