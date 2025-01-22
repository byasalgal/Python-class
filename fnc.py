# def asd():
#     print("sjkudxfzumjkdfxlikdfru,k")

# asd()
# print("byasalgal")
# asd()5856487546747
# def add(a,b):
#     # print(a + b)
#     # print(">:()")
#     return a+b


# print (add(int(input("1numb: ")),int(input("2numb: "))))
def ad(a,b):
    return a+b

def ms(a,b):
    return a-b

def di(a,b):
    return a//b

def mlt(a,b):
    return a*b

print("select option: \na.+ \nb.- \nc./ \nd.*")
option1 = input("select choise: ")
nmb1 = int(input("Enter 1 number: "))
nmb2 = int(input("Enter 2 number: "))
if option1 == "a":
    print(ad(nmb1,nmb2))
elif option1 == "b":
    print(ms(nmb1,nmb2))
elif option1 == "c":
    print(di(nmb1,nmb2))
elif option1 == "d":
    print(mlt(nmb1,nmb2))
else:
    print("option incorrect")