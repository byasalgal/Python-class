number1 = int(input("enter 1st number = "))
number2 = int(input("enter 2nd number = "))
number3 = int(input("enter 3th number = "))
if number1 > number2 and number1 > number3:
    print (number1 , "is greater than other number")
elif number2 > number1 and number2 > number3:
    print (number2 , "is greater than other number")
elif number3 > number1 and number3 > number2:
    print (number3 , "is greater than other number")
else:
    print ("every number is same")

if number1 > number2:
    if number1 > number3:
        print("number1 is greater")