# The code will simulate the soldout of some cinema tikets

N_OF_TIKETS = 100
CONST_MAX_FOR_USER = 4
users = 0

while N_OF_TIKETS > 0:
    tikets = int(input("Enter the numer of tikets you want to buy... "))
    while tikets > 4:
        print("You cannot buy more then 4 tikets... ")
        tikets = int(input("Enter the numer of tikets you want to buy... "))
    N_OF_TIKETS = N_OF_TIKETS - tikets
    print("There are ", N_OF_TIKETS, " left...")
    users = users + 1
print("There are no more tikets to buy...")
print("Users: ", users)
