lisk = [1,999,324,567,7832]
asd = []
dsd = []
for i in range(len(lisk)):
    print(lisk[i])
    if lisk[i] % 2 == 0:
        asd.append(lisk[i])
    else:
        dsd.append(lisk[i])

print(f"even: {asd} \n odd: {dsd}")