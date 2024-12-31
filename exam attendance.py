medicalcause= str(input("do you have medical cause y for yes n for no: "))
attendance= int(input("enter your attendancy: "))
if medicalcause == "y":
    print("You can take the exam")
elif medicalcause == "n":
    if attendance > 75:
        print("You can take the exam")
    else:
        print("You cannot take the exam, attendance lower than 75")
else:
    print("response invalid")