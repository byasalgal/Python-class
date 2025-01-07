number1 = int(input("Enter the number you want to power: "))
number2 = int(input("Enter the exponent: "))

result = 1  # Initialize result to 1 (neutral element for multiplication)
for i in range(number2):  # Loop runs `number2` times
    result *= number1  # Multiply result by number1 in each iteration

print("The answer is:", result)
