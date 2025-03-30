# class Apple:
#     def __init__(self,name,type):
#         self.name = name
#         self.type = type

# obj = Apple("Apple","Fruit")
# print(obj.name , obj.type)
# class Apple:
#     def __del__(self):
#         print("destroyed")

# obj = Apple()

# del obj
# l1 = ["eat","sleep","reapet"]
# obj1 = enumerate(l1)
# print(list(enumerate(l1)))
class IOString:
    def __init__ (self,str1):
        self.str1 = str1
    
    def answert(self):
        self.str1 = input("enter anything to convert into uppercase: \n")

    def uppercase(self):
        print(self.str1.upper())

obj = IOString("Asd")
obj.answert()
obj.uppercase()