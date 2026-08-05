class Vehicle:
    def __init__(self, b, ms):
        self.b = b   
        self.ms = ms
    def st(self):
        print("Brand: ", self.b)
        print("Max speed: ", self.ms, "km/h")    

class car(Vehicle):
    def __init__(self, m, s, b, ms):
        self.m = m
        self.s = s
        super().__init__(b, ms)

    def st(self):
        print("Model:", self.m)
        print("Seats:", self.s)
        super().st()

    def fh(self, fuel):
        print(self.m, "uses", fuel)

ch = car("City rider", 5, "Honda", 180)
ch.st()
ch.fh("petrol")

print("Is car a subclass of Vehicle?", issubclass(car, Vehicle))