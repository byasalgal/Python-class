import random
number1 = str(input())
number2 = str(input())
number3 = str(input())
strings = [number1, number2, number3]
random.shuffle(strings)
print("Randomized order:", strings)