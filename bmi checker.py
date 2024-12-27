weight = float(input("enter your weight in kg : "))
height = float(input("enter your height in m : "))
bmi = weight / (height**2)
if bmi < 18.5:
    print("U are underweight. Ur bmi is : " , bmi)
elif bmi > 18.5 and bmi < 24.9:
    print("U are normal. Ur bmi is : " , bmi)
elif bmi > 25 and bmi < 29.9:
    print("U are overweight. Ur bmi is : " , bmi)
elif bmi > 30 and bmi < 34.9:
    print("U are obese. Ur bmi is : " , bmi)
elif bmi > 34.9:
    print("U are  extremely obese. Ur bmi is : " , bmi)