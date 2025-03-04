inpit = input("enter a word or number")
dfg = ""
for i in range(len(inpit)-1,-1,-1):
    dfg = dfg+inpit[i]

print(dfg)
if inpit == dfg:
    print("palendrum")
else:
    print("not palendrum")