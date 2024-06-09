number3=input("Enter Number")#Read input from user
number1 = int(number3)#convert String into integer

number4 = input("Enter number")
number2 = int(number4)

# print(number3 + number4) 
operator = input("Enter operator")

if(operator == "+"):
    print(number1 + number2) 

if(operator == "-"):
    print(number1-number2)

if(operator == "*"):
    print(number1*number2)

if(operator == "/"):
    print(number1/number2)

exit