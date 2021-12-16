# The code will do stuff on two string

alphabeth = [chr(i) for i in range(97, 123)]

string1 = input("Type the first word... ")
string2 = input("Type the second word... ")

def compare(string1: str, string2: str):
    string1 = set(string1)
    string2 = set(string2)
    both = string1 & string2 # Logic and
    only_one = string1 ^ string2 # Logic Xor
    neither = set(alphabeth).difference(both).difference(only_one)
    
    return(both, only_one, neither)

print(compare(string1, string2))
