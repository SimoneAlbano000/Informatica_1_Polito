# The code will do stuff with a typed string

typed_string = input("Type a string... ")

# Print upper chars
for i in typed_string:
    if i.isupper():
        print("Is upper: ", i)

print(typed_string[1::2])

new_string = []

for i in range(len(typed_string)):
    if typed_string[i] in "aeiou":
        new_string.insert(i, "_")
    else:
        new_string.insert(i, typed_string[i])
print(new_string)


#Print dec chars
dec = 0
for i in typed_string:
    if i.isdecimal():
        dec = dec + 1
print("Decimal chars: ", dec)

# Print vocals indexes:
for i in range(len(typed_string)):
    if typed_string[i] in "aeiou":
        print("Vocals index: ", i)







