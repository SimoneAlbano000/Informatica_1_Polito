# The code will ask for n int and check for the magic square

var = []
var_table = []
table_dimension = int(input("Insert the square dimension... "))
magic_n = int(input("Insert magic number... "))

# Check if the input is valid
while sorted(var) != [i for i in range(1, table_dimension**2 + 1)]:
    var = []
    for i in range(table_dimension**2):
        var.append(int(input("Type a number... ")))

# Convert from list to table
for i in range(table_dimension):
    var_table.append(var[table_dimension*i:table_dimension*i + table_dimension])

# Check all conditions
if (
    # Rows ok
    list(sum(var_table[i]) for i in range(table_dimension)) == [magic_n for i in range(table_dimension)]
    and
    # Columns ok
    list(sum(var_table[i][j] for i in range(table_dimension)) for j in range(table_dimension)) == [magic_n for i in range(table_dimension)]
    and
    # Diagonals ok
    list(sum(var_table[i][(i*j)+j] for i in range(table_dimension)) for j in [0, -1]) == [magic_n for i in range(2)]
):
    print("Rows, Columns and Diagonals ok...")
else:
    print("This is not a magic square...")