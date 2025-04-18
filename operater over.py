# class Point:
#     def __init__ (self,x=0,y=0):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return "({0} ({1}".format(self.x , self.y)
    
#     def __add__ (self,other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Point(x,y)
    
# P1 = Point(1,2)
# P2 = Point(2,3)
# print(P1+P2)
class Smth:
    def __init__(self,a):
        self.a = a

    def __lt__(self,other):
        if (self.a < other.a):
            return "yes a<a"
        else:
            return "no a<a"
        
    def __eq__(self,other):
        if (self.a == other.a):
            return "yes a=a"
        else:
            return "no a=a"
        

p1 = Smth(1)
p2 = Smth(2)

print(p1 < p2)
print(p1 == p2)