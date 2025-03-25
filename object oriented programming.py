# class fruit:
#     print("blah blah blah")
#     def __init__(self,name):
#         self.name = name

# apple = fruit("apple")
# banana = fruit("banana")

# print(apple.name)
# print(banana.name)
# #class student:
# #     def __init__(self,name,grade):
# #         self.name = name
# #         self.grade = grade
# # stukent = student(5,"smth")
# # print(stukent.name , stukent.grade)
class Parrot:
    def __init__(self,name,age):
        self.name = name
        self.age = age

smth = Parrot(input("enter name for parrot: \n") , int(input("enter age of parrot: \n")))
print(smth.age , smth.name)