# dumb exercise

def calcTaxes(money, children):
    if 30E3 <= money < 40E3 and children >= 3:
        return 10E2
    elif 20E3 <= money < 30E3 and children >= 2:
        return 15E2
    elif money < 20E3:
        return 20E2

def main():
    money = int(input("Type ISEE... "))
    children = int(input("Type number of children... "))

    print("money: ", calcTaxes(money, children))

    return 0

main()