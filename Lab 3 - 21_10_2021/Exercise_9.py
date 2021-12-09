# The code will calculate the value of a cupon code based on the user input

var = int(input("Type the cost..."))

if var <= 10 :
    print("No cupon...")
elif 10 < var <= 60 :
    print("Coupon: ", var*0.08)
elif 60 < var <= 150 :
    print("Coupon: ", var*0.1)
elif 150 < var <= 210 :
    print("Coupon: ", var*0.12)
elif var > 210 :
    print("Coupon: ", var*0.14)
