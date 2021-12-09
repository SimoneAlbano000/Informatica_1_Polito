# Simple func

def countVowels(val):
    vocals = 0
    for i in val:
        if i in "aeiou":
            vocals += 1
    return vocals

def main(): 

    user_input = input("Type a string...")
    print(countVowels(user_input))

    return 0

main()