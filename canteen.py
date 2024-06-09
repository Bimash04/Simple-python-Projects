menu= {
    "momo": 120,
    "pizza":350,
    " c burgeer":200,
    "birayni": 250,
    "laphing":150,
    "chamouin":100,
    "c momo":100,
    "fried momo":160,
     "veg burger":100   
}

print ("Wlecome to our canteen.")
print ("momo: 120\npizza: 350\nc burgeer:200\n birayni: 250\nlaphing:150\nc momo:100\nfried momo:160\nveg burger:100")

totalOrders = 0

firstItems= input("Enter the order you wish to order=")

if firstItems in menu:
    totalOrders = menu[firstItems]
    print (f"Your first order{firstItems} has been added to your order list")
else : 
    print (f"Please select the order you wish {firstItems} to order that has been in our menu list:")
    
anotherOrder = input("DO you want to order more than one item?(y/n)")
if anotherOrder=='y':
    secondItem =  input("Enter the second item you wish to ordrs =  ")
    if secondItem in menu:
        totalOrders += menu[secondItem]
        print (f"Your second {secondItem} has been added to orders")
    else:
        print (f"Please select the order you wish {secondItem} to order that has been in our menu list:")
print (f"The total amount of orders item is {totalOrders}")

    