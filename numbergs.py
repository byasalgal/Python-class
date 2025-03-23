import random as rd
Name = input("Whats your name: \n")
print(f"{Name},lets play a number guessing game")
Number = rd.randint(1,100)
print("Thinked of a number guess it now \n 1-100")
if Number %2 == 0:
    print("Its a even number")
else:
    print("Its a odd number")
guess = int(input("Guess the number: \n"))
tried = 0
while tried < 5:
    if guess > Number:
        print("Lower")
        tried = tried+1
    elif guess < Number:
        print("Higher")
        tried = tried+1
    else:
        print("Correct")
        break

    guess = int(input("Guess the number: \n"))

if tried == 5:
    print("You used up your 5 chances.Goodbye")

