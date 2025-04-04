import math

class circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius

radius = float(input("enter the radius of the circle: "))
my_circle = circle(radius)

print("area of the circle:", my_circle.area())
print("perimeter of the circle:", my_circle.perimeter())