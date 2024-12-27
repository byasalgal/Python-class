grade1 = int(input("enter marks : "))
grade2 = int(input("enter marks : "))
grade3 = int(input("enter marks : "))
grade4 = int(input("enter marks : "))
grade5 = int(input("enter marks : "))
average = (grade1 + grade2 + grade3 + grade4 + grade5) // 5
print ("average is : " , average)
if average > 91 & average < 100:
    print("grade is a")
elif average > 81 & average < 90:
    print("grade is b")
elif average > 71 & average < 80:
    print("grade is c")
elif average > 61 & average < 70:
    print("grade is d")
elif average < 60:
    print("grade is F")