# # for i in range(10,0,-1):
# #     if i == 5:
# #         # continue    
# #         break
    
# #     print(i)
    
# # def  jfr():
# #     pass

# # jfr()
# asdf = "coding"
# for i in range(len(asdf)):
#     if asdf[i]  ==  "i":
#         break

#     print(asdf[i])

for i in range(1,21):
    if i %5 ==  0 and i %3 == 0:
        print("fizzbuzz")
    elif i %5 == 0:
        print("buzz")
    elif i %3 == 0:
        print("fizz")
    else:
        print(i)