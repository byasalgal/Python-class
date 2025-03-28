class dog:
    animal = "dog"

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def show(self):
        print("name:", self.name)
        print("breed:", self.breed)
        print("animal:", dog.animal)

dog1 = dog("buddy", "labrador")
dog2 = dog("max", "beagle")

dog1.show()
print()
dog2.show()
