# dicto = {"happy":0 , "sad":1 , "angry":0}
# print(dicto)
# print(type(dicto))
# print(len(dicto))
# print(dicto.keys())
# print(dicto.values())
# print(dicto["sad"])
# dicto["sad"] = "iooooapps"
# print(dicto["sad"])
# for i in dicto:
#     print(dicto[i])
af = {"jiikl":567 , "hjiikl":1234 , "giikl":567}
temp = 567
k = 0
for i in af.values():
    if i == temp:
        k+=1

print(k)