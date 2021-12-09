# The code will search specific words among different files

file_list = ("data.txt", "dictionary.txt")
found = []

word = input("Please type the word you wanna find... ")

for i, file_name in enumerate(file_list):
    with open(file_name, "r") as file_name:
        for line in file_name:
            if word in line:
                found.append([file_list[i], line, word])

print(found)

        