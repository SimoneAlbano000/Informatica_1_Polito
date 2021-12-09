 # The code will merge two list

list_1 = [1, 3, 5, 7, 9]
list_2 = [2, 4, 6, 8, 10, 12, 14]

def merge(a: list, b:list):
    # Tuple containing the n° element of the shortest list and a copy of the two list
    data = (min(len(a), len(b)), max(a, b), min(a, b))
    c = list(data[1])
    
    for i in range(data[0]):
       c.insert(2*i, data[2][i])
    
    return c

print(merge(list_1, list_2))
