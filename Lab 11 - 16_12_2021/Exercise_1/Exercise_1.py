# The code will count words occurencies in a file

import sys

with open(f"{sys.path[0]}\\data.txt", "r") as data:
    dict = {}
    for line in data:
        words = line.strip().split()
        for i in words:
            if i in dict:
                dict[i] = dict[i] + 1
            else:
                dict[i] = 1      
print(dict)
