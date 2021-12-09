# The code will identify the season wiht a given input that corrispond to the month

season_table = ["Winter", "Spring", "Summer", "Fall"]

month = int(input("Type the month number..."))
day = int(input("Type the month number..."))

if month == 1 or month == 2 or month == 3 :
    if month%3 == 0 and day > 21 :
       print(season_table[1])
    else :
        print(season_table[0])
elif month == 4 or month == 5 or month == 6 :
    if month%3 == 0 and day > 21 :
       print(season_table[2])
    else :
        print(season_table[1])
elif month == 7 or month == 8 or month == 9 :
    if month%3 == 0 and day > 21 :
       print(season_table[3])
    else :
        print(season_table[2])
elif month == 10 or month == 11 or month == 12 :
    if month%3 == 0 and day > 21 :
       print(season_table[0])
    else :
        print(season_table[3])
