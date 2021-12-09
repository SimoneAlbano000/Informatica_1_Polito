# The code will transform any given tring in the form x1x2x3...x4x5x6

CONST_STRING = "test_string"

if len(CONST_STRING) < 6:
    print("Error")
else:
    print(CONST_STRING[:3] + "..." + CONST_STRING[-3:])