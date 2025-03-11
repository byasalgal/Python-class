import array as aray
mint = aray.array("i",[1,1,2,4,3])
print(mint)
print(type(mint))
print(mint[3])
mint.append(21)
print(mint)
for i in range(len(mint)):
    print(mint[i])

mint.reverse()
print(mint)