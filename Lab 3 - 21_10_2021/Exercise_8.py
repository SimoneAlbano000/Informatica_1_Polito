# The code will convert the input value

liquid_unit_table = ["ml", "l", "fl", "gal"]
liquid_vals_table = [1E-3, 1, 33.814, 0.264] 
weight_unit_table = ["g", "kg", "lb", "oz"]
weight_vals_table = [1E-3, 1, 2.205, 35.274]
distances_unit_table = ["mm", "cm", "m", "km", "in", "ft", "mi"]
distances_vals_table = [1E-3, 1E-2, 1, 1E3, 39.370, 3.281, 0.622]

from_input = input("Convert from?...")
to_input = input("Convert to?...")
value = float(input("Value..."))

if from_input in liquid_unit_table and to_input in liquid_unit_table and (liquid_unit_table.index(to_input) - liquid_unit_table.index(from_input)) != 1 :
    if liquid_unit_table.index(from_input) < liquid_unit_table.index(to_input) :
        print(value*(liquid_vals_table[liquid_unit_table.index(from_input)]*(liquid_vals_table[liquid_unit_table.index(to_input)])))
    else : 
        print(value/(liquid_vals_table[liquid_unit_table.index(from_input)]*(liquid_vals_table[liquid_unit_table.index(to_input)])))

elif from_input in weight_unit_table and to_input in weight_unit_table and (liquid_unit_table.index(to_input) - liquid_unit_table.index(from_input)) != 1:
    if weight_unit_table.index(from_input) < weight_unit_table.index(to_input) :
        print(value*(weight_vals_table[weight_unit_table.index(from_input)]*(weight_vals_table[weight_unit_table.index(to_input)])))
    else : 
        print(value/(weight_vals_table[weight_unit_table.index(from_input)]*(weight_vals_table[weight_unit_table.index(to_input)])))

elif from_input in distances_unit_table and to_input in distances_unit_table and (liquid_unit_table.index(to_input) - liquid_unit_table.index(from_input)) != 1 :
    if distances_unit_table.index(from_input) < distances_unit_table.index(to_input) :
        print(value*(distances_vals_table[distances_unit_table.index(from_input)]*(distances_vals_table[distances_unit_table.index(to_input)])))
    else : 
        print(value/(distances_vals_table[distances_unit_table.index(from_input)]*(distances_vals_table[distances_unit_table.index(to_input)])))
else :
    print("Conversion not supported...")