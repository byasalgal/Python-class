# def mli(f,s):
#     print(f,s)

# mli(s=input("Enter first name:"),f=input("Enter second name:"))
# numb =5
# for i in range(numb-1,0,-1):
#     numb= numb*i

# print(numb)
def fco(l):
    if l == 0   or l==1:
        return 1
    else:
        return  l*fco(l-1)

print(fco(1))