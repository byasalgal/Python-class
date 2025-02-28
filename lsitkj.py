iop = ["o i a","pew","berg0","dhf","dfh"]
print(iop)
print(iop[2]) #indexing
print(iop[-1:-4])
for i in range (len(iop)):
    print(iop[i])

iodA = ["o SA a","peJHG","berg0","dhDSA","dSADh"]
print(iop + iodA)
iop.extend(iodA)
print(iop)
njsdf= [13,876,1,78]
njsdf.sort()
temp = 0
print(njsdf[0])
print(njsdf[len(njsdf) - 1])
for i in range(len(njsdf)):
    temp = temp + njsdf[i]

print(temp/len(njsdf))