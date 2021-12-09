# Banking account system

def calcInterests(years, balance_0, annual_increment):
    for i in range (years):
        balance_0 += balance_0*(annual_increment/100)
    return balance_0

years = int(input("Type the number of years... "))
balance_0 = int(input("Type the initial balance... "))
annual_increment = int(input("Type the annual increment in %... "))

print(calcInterests(years, balance_0, annual_increment))