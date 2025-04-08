class vehicle:
    def __init__(self, seating_capacity):
        self.seating_capacity = seating_capacity

    def fare(self):
        return self.seating_capacity * 100

class bus(vehicle):
    def fare(self):
        basic_fare = super().fare()
        maintenance_charge = basic_fare * 0.1
        total_fare = basic_fare + maintenance_charge
        return total_fare

bus = bus(50)
print("total bus fare: inr", bus.fare())