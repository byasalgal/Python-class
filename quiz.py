print ("how many people are living in the world")
print ("1.7B \n2.8B \n3.3B \n4.9B")
answer = int(input("Choose numbers above : "))
if answer == 2:
    print("Correct")
elif answer == 1 or answer == 3 or answer == 4:
    print ("Incorrect")
else:
    print("Number is outside of options")