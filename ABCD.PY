from abc import ABC , abstractmethod
# class Abs(ABC):
#     def prtn(self,value):
#         print(value)

#     @abstractmethod
#     def Invisible(self):
#         print("i am invisible")

# class secnd(Abs):
#     def Invisible(self):
#         print("i am inside sub class")

# t = secnd()
# t.prtn(12)
# t.Invisible()




# class Animal(ABC):
#     def dog(self):
#         print("im a living being")

#     @abstractmethod
#     def move(self):
#         print("i am a human")

# class Dog(Animal):
#     def move(self):
#         print("smth happened")

# t = Dog()
# t.dog()
# t.move()





class Usa():
    def Capital(self):
        print("Washington D.C is the capital of Usa")

    def Language(self):
        print("Enlish is the most used and primary language of Usa")

    def Type(self):
        print("Usa is a developed country")

class Russia():
    def Capital(self):
        print("Moscow is the capetal of Russia")

    def Language(self):
        print("Russian is the most used and primary language of Russia")

    def Type(self):
        print("Russia is a developed country")

obj_USA = Usa()
obj_RUS = Russia()
for country in (obj_USA , obj_RUS):
    country.Capital()
    country.Language()
    country.Type()