input1 = int(input("enter 1st clothe tempature"))
input2 = int(input("enter 2nd clothe tempature"))
input3 = int(input("enter 3rt clothe tempature"))
input4 = int(input("enter 4rt clothe tempature"))
input5 = int(input("enter 5rt clothe tempature"))
Cold_tempature = 10
if input1 > Cold_tempature:
    print("1 clothe")
elif input2 > Cold_tempature:
    print("2 clothe")
elif input3 > Cold_tempature:
    print("3 clothe")
elif input4 > Cold_tempature:
    print("4 clothe")
elif input5 > Cold_tempature:
    print("5 clothe")
else:
    print("No clothe are suitable")