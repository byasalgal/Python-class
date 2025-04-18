class BMW:
    def fuel_type(self):
        print("BMW uses petrol")

    def max_speed(self):
        print("BMW max speed is 250 km/h")


class Ferrari:
    def fuel_type(self):
        print("ferrari uses petrol")

    def max_speed(self):
        print("ferrari max speed is 340 km/h")

def show_car_details(car):
    car.fuel_type()
    car.max_speed()

bmw_car = BMW()
ferrari_car = Ferrari()
print("BMW Details:")
show_car_details(bmw_car)

print("\nferrari Details:")
show_car_details(ferrari_car)
