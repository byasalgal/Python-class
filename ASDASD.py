ognumber=int(input("enter a random 3digit n"))
sum=0
temp=ognumber
while temp>0:
    rem = temp%10
    sum=rem**3+sum
    temp= temp//10

    
if sum==ognumber:
    print("yes")
else:
    print("no")