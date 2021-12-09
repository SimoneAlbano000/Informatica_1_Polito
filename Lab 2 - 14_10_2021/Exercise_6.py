# The code will format a string that contain a phone number

CONST_COUNTRY_CODE = "+39" # Italy

phone_number = str(input("Type the phone number..."))
formatted_phone_number = CONST_COUNTRY_CODE + " " + "(" + phone_number[:3] + ")" + " " + phone_number[3:6] + "-" + phone_number[6:]

print(formatted_phone_number)