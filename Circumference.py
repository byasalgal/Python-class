def find_circumference(radius):
    pi = 3.1415
    return 2 * pi * radius

radius = float(input("enter the radius of the circle: "))

circumference = find_circumference(radius)
print(f"the circumference of the circle is: {circumference:.2f}")
