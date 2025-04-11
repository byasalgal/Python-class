# class Privatevar:
#     __Privatl = 7
#     def __init__(self,somting):
#         self.somting = somting

#     def __Privmeth(self):
#         print(self.somting)
#     def hello(self):
#         print(Privatevar.__Privatl)

# obj = Privatevar(input("Enter somthing to vault"))
# obj.hello()
class computer:
    def __init__(self):
        self.__maxprice = 900

    def display(self):
        print(self.__maxprice)

    def set(self,an):
        self.__maxprice = an

c=computer()
c.display()
c.set(int(input("Enter max price: ")))
c.display()