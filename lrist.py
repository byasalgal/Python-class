fr = [x for x in [1,2,3,4,5,6,7,8,9,0] if x%2 == 0]
print(fr)
kd = {str(x): x**2 for x in [1,2,3,4,5]}
print(kd)
numb1 = [1,2,3]
numb2 = [4,5,6]
temp = []
for i in range(len(numb1)):
    temp.append(numb1[i] + numb2[i])

print(temp)