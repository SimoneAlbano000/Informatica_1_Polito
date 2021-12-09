# The code will manage a cinema tiket list 

from random import randint as laputtanadellamamma

prize_table = [[10 for i in range(10)] for j in range(3)]
prize_table.append([10, 10, 20, 20, 20, 20, 20, 20, 10, 10])
prize_table.append([10, 10, 20, 20, 20, 20, 20, 20, 10, 10])
prize_table.append([10, 10, 20, 20, 20, 20, 20, 20, 10, 10])
prize_table.append([20, 20, 30, 30, 40, 40, 30, 30, 20, 20])
prize_table.append([20, 30, 30, 40, 50, 50, 40, 30, 30, 20])
prize_table.append([30, 40, 50, 50, 50, 50, 50, 50, 40, 30])

selection = int(input("prize or sit? (0/1)"))

if selection == 0:
    var = int(input("How much do you wanna spend for the ticket? "))
    print("available sits: ")

    for i in range(len(prize_table)):
        print(prize_table[i])

elif selection == 1:
    pass

# To be finished
