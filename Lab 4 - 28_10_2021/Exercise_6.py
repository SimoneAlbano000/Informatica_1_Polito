# The code will print out all the substrings of "string"

string = input("Type a string... ")

for i in range(len(string)):
    for j in range(0, len(string) - i, 1):
        print(string[j:j+i+1:1])

# Example:
    # input: 
        # "hello"
    # output:
        # h
        # e
        # l
        # l
        # o
        # he
        # el
        # ll
        # lo
        # hel
        # ell
        # llo
        # hell
        # ello
        # hello
