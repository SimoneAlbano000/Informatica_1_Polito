# Conversion between roman and arabic values

roman_table = ["I", "V", "X", "L", "C", "D", "M"]
arabic_table = [1, 5, 10, 50, 100, 500, 1000]

def roman2arabic(roman):
    out = 0
    val_dictionary = []
    for i in roman:
        val_dictionary.append(arabic_table[roman_table.index(i)])
    for j in range(len(val_dictionary) - 1):
        if val_dictionary[j] >= val_dictionary[j + 1]:
            out += val_dictionary[j]
        elif val_dictionary[j] < val_dictionary[j + 1]:
            out -= val_dictionary[j]
    return out + val_dictionary[j + 1]

roman = input("Type a roman number... ")
print(roman2arabic(roman))