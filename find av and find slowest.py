biker1 = int(input("enter biker1 speed : "))
biker2 = int(input("enter biker2 speed : "))
biker3 = int(input("enter biker3 speed : "))
average = (biker1 + biker2 + biker3) // 3
if biker1 < average:
    print ("biker 1 is slower than average")
elif biker2 < average:
    print ("biker 2 is slower than average")
elif biker3 < average:
    print ("biker 3 is slower than average")