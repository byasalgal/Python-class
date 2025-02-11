def aagefind():
    try:
        sword = float(input("enter your age : "))
        if  sword%2==1:
            print("ur age is odd")
        else:
            print("ur age is even")
    except ValueError:
        print("couldnt procces due to user error")
        return("no")
    
while True:
    if aagefind() == "no":
        aagefind()