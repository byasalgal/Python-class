actual_price = int(input("Actual price : "))
sell_price = int(input("Sell price : "))
if sell_price > actual_price:
    print(sell_price - actual_price , "profit")
else:
    print(actual_price - sell_price , "loss")