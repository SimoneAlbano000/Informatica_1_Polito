# Func to find number of words in string

def countWords(val):
    spaces = 0
    for i in range(len(val) - 1):
        if val[i] == " " and val[i + 1] != " ":
            spaces += 1
    return spaces + 1

def main():

    user_input = input("Type a string... ")
    print(countWords(user_input))

    return 0

main()