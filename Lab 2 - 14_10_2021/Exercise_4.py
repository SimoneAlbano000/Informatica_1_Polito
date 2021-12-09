# The code will replace an obsolate old men in a library

CONST_TAX_x100 = 1.075 # Equivalent to 107.5%
CONST_SHIPPING_COST_XBOOK = 2

books_n = int(input("Type the number of books..."))
total_cost = int(input("Type the total book cost..."))

cost_x_book = total_cost/books_n


print("Total cost: ", + ((cost_x_book+CONST_SHIPPING_COST_XBOOK)*books_n)+total_cost*CONST_TAX_x100)