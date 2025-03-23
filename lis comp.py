num = int(input("enter a number: "))
odd_numbers = [i for i in range(num) if i % 2 != 0]
print("odd numbers less than", num, "are:", odd_numbers)

fruits = ["apple", "banana", "mango", "orange"]
capitalized_fruits = [fruit.capitalize() for fruit in fruits]
print("capitalized fruit names:", capitalized_fruits)