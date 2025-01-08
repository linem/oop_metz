class Trip:
    def __init__(self, bicycles, customers, vehicle):
        self.bicycles = bicycles
        self.customers = customers
        self.vehicle = vehicle

    def prepare(self, mechanic):
        mechanic.prepare_bicycles(self.bicycles)


class Mechanic:
    def prepare_bicycles(self, bicycles):
       for bicycle in bicycles:
           self.prepare_bicycle(bicycle)

    def prepare_bicycle(self, bicycle):
        print(f"Bike {bicycle} is ready!")


once_in_a_lifetime_trip = Trip(["b1", "b2"],  "c", "v")
worlds_best_mechanic = Mechanic()

once_in_a_lifetime_trip.prepare(worlds_best_mechanic)