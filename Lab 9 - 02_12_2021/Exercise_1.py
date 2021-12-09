# The code will do some stupid operation on lists

example_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# a

def change_firts_last(var: list):
    var = list(var)
    var[0], var[-1] = var[-1], var[0]
    return var

print(change_firts_last(example_list))

# c

def replace_even_zero(var: list):
    var = list(var)
    for i, j in enumerate(var):
        if j % 2 == 0:
            var[i] = 0
    return var

print(replace_even_zero(example_list))

#d

def replace_with_biggest(var: list):
    # Create two copies of the original list,
    # one for reference and the other to be modified
    var = list(var)
    reference_var = list(var)

    # Exclude first and last elements
    for i in range(1, len(var) - 1):
        var[i] = max(reference_var[i - 1], reference_var[i + 1])

    return var

print(example_list)
print(replace_with_biggest(example_list))
print(example_list)
