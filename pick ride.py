ride=int(input("pick rides: \n1.bike \n2.car \nSelect option: "))
if ride == 2:
    print("You have selected Car")
else:
    option2=int(input("Choose which bike: \n1.Scooty \n2.scooter \n3.bicycle \n4.motorcycle \nSelect option: "))
    if option2 == 1:
        print("you have choosed Scooty")
    elif option2 == 2:
        print("you have choosed Scooter")
    elif option2 == 3:
        print("you have choosed bicycle")
    else:
        print("you have choosed motorcycle")