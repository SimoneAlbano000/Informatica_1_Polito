# The code will tell if a given year is bisestile or not

year = int(input("Type the year..."))

if (year%4 == 0 or year%400 == 0) and year%100 != 0 :
    print("Bisestile")
else : 
    print("Non Bisestile")
