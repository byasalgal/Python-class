tup1 = (4,3,2,-1,18)
tup2 = (2,4,8,8,3,2,9)
temp = tup1[0]
for i in range(len(tup1)):
    temp*= tup1[i]

print(temp)
temp = tup2[0]
for i in range(len(tup2)):
    temp*= tup2[i]

print(temp)