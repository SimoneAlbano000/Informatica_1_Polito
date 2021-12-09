# Nim

from random import *
new_game = 1

while new_game == 1:

    INITIAL_MARBLES = randint(10, 100)
    CONST_CPU_GAME_STYLE = randint(0, 1) # 0 = stupid, 1 = smart
    CONST_FIRST_USER = randint(0, 1) # 0 = user, 1 = cpu

    match str(CONST_CPU_GAME_STYLE) + str(CONST_FIRST_USER):

        case "00":
            # user start with stupid cpu
            while INITIAL_MARBLES > 0:
                print("\n")
                print("There are ", INITIAL_MARBLES, " marbles...")

                user_marbles = int(input("How many marbles do you want? "))
                while user_marbles > int(INITIAL_MARBLES/2):
                    print("You can take max", int(INITIAL_MARBLES/2), " marbles...")
                    user_marbles = int(input("How many marbles do you want? "))
                INITIAL_MARBLES = INITIAL_MARBLES - user_marbles
                if INITIAL_MARBLES == 1:
                    print("You have win...")
                    break
                
                if INITIAL_MARBLES == 2:
                    cpu_marbles = 1
                else:
                    cpu_marbles = randint(1, int(INITIAL_MARBLES/2))

                print("The cpu has taken ", cpu_marbles, " marbles...")
                INITIAL_MARBLES = INITIAL_MARBLES - cpu_marbles
                if INITIAL_MARBLES == 1:
                    print("You have lost...")
                    break
        
        case "11":
            # cpu start with smart cpu
            while INITIAL_MARBLES > 0:
                print("\n")
                print("There are ", INITIAL_MARBLES, " marbles...")

                if INITIAL_MARBLES == 2:
                    cpu_marbles = 1
                elif INITIAL_MARBLES in [3, 7, 15, 31, 63]:
                    print("power of two -1") # for debug 
                    cpu_marbles = randint(1, int(INITIAL_MARBLES/2))
                else:
                    cpu_vals = []
                    for i in [3, 7, 15, 31, 63]:
                        if INITIAL_MARBLES - i > 0:
                            cpu_vals.append(INITIAL_MARBLES - i)
                    cpu_marbles = min(cpu_vals)

                print("The cpu has taken ", cpu_marbles, " marbles...")
                INITIAL_MARBLES = INITIAL_MARBLES - cpu_marbles
                if INITIAL_MARBLES == 1:
                    print("You have lost...")
                    break

                user_marbles = int(input("How many marbles do you want? "))
                while user_marbles > int(INITIAL_MARBLES/2):
                    print("You can take max", int(INITIAL_MARBLES/2), " marbles...")
                    user_marbles = int(input("How many marbles do you want? "))
                INITIAL_MARBLES = INITIAL_MARBLES - user_marbles
                if INITIAL_MARBLES == 1:
                    print("You have win...")
                    break

        case "01":
            # cpu start and is stupid
            while INITIAL_MARBLES > 0:
                print("\n")
                print("There are ", INITIAL_MARBLES, " marbles...")

                if INITIAL_MARBLES == 2:
                    cpu_marbles = 1
                else:
                    cpu_marbles = randint(1, int(INITIAL_MARBLES/2))

                print("The cpu has taken ", cpu_marbles, " marbles...")
                INITIAL_MARBLES = INITIAL_MARBLES - cpu_marbles
                if INITIAL_MARBLES == 1:
                    print("You have lost...")
                    break

                user_marbles = int(input("How many marbles do you want? "))
                while user_marbles > int(INITIAL_MARBLES/2):
                    print("You can take max", int(INITIAL_MARBLES/2), " marbles...")
                    user_marbles = int(input("How many marbles do you want? "))
                INITIAL_MARBLES = INITIAL_MARBLES - user_marbles
                if INITIAL_MARBLES == 1:
                    print("You have win...")
                    break
                
        case "10":
            # user start with smart cpu
            while INITIAL_MARBLES > 0:
                print("\n")
                print("There are ", INITIAL_MARBLES, " marbles...")

                user_marbles = int(input("How many marbles do you want? "))
                while user_marbles > int(INITIAL_MARBLES/2):
                    print("You can take max", int(INITIAL_MARBLES/2), " marbles...")
                    user_marbles = int(input("How many marbles do you want? "))
                INITIAL_MARBLES = INITIAL_MARBLES - user_marbles
                if INITIAL_MARBLES == 1:
                    print("You have win...")
                    break
                
                if INITIAL_MARBLES == 2:
                    cpu_marbles = 1
                elif INITIAL_MARBLES in [3, 7, 15, 31, 63]:
                    print("power of two -1") # for debug 
                    cpu_marbles = randint(1, int(INITIAL_MARBLES/2))
                else:
                    cpu_vals = []
                    for i in [3, 7, 15, 31, 63]:
                        if INITIAL_MARBLES - i > 0:
                            cpu_vals.append(INITIAL_MARBLES - i)
                    cpu_marbles = min(cpu_vals)

                print("The cpu has taken ", cpu_marbles, " marbles...")
                INITIAL_MARBLES = INITIAL_MARBLES - cpu_marbles
                if INITIAL_MARBLES == 1:
                    print("You have lost...")
                    break
    new_game = int(input("Do you want to play again? (1/0) "))
