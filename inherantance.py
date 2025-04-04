class dad():
    def __init__ (self,eyes,aggresave):
        self.eyes = eyes
        self.aggresave = aggresave

    def display(self):
        print(f"your eye color is {self.eyes}")
        print(f"you are aggrisave {self.aggresave}")


class son(dad):
    def __init__ (self,name,age,eyes,aggresave):
        self.name = name
        self.age = age
        dad.__init__(self,eyes,aggresave)

obj = son("Penguin",8,"Blue",True)


obj.display()
print(issubclass(dad,son))