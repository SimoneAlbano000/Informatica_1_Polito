# The code will work on a csv file for managing tikets

import sys

def check_integrity():

    try:
        record_file = open(f"{sys.path[0]}\\record.txt", "r")
    except FileNotFoundError:
        print("Record file not found... ")
        print("Creating empty record file... ")
        record_file = open(f"{sys.path[0]}\\record.txt", "w")
        record_file.close()
        record_file = open(f"{sys.path[0]}\\record.txt", "r")

    for line in record_file:
        if line.count(";") != 3:
            return False
    return True

def calc_cost():

    try:
        record_file = open(f"{sys.path[0]}\\record.txt", "r")
    except FileNotFoundError:
        print("Record file not found... ")
        print("Creating empty record file... ")
        record_file = open(f"{sys.path[0]}\\record.txt", "w")
        record_file.close()
        record_file = open(f"{sys.path[0]}\\record.txt", "r")

    table = {}
    for line in record_file:
        if line.split(";")[1] in table.keys():
            table[line.split(";")[1]] = int(line.split(";")[2]) + int(table.get(line.split(";")[1]))
        else:
            table[line.split(";")[1]] = int(line.split(";")[2])
    return table

if check_integrity() == True:
    print(calc_cost()) 
else:
    print("File integrity issue...")