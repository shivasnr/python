class Vehicle:
    def __init__(self, started = False, speed = 0):
        self.started = started
        self.speed = speed
    def start(self):
        self.started = True
        print("Started, let's ride!")
    def stop(self):
        self.speed = 0
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print("Vrooooom!")
        else:
            print("You need to start me first")

# redefine our Car class, using inheritance
class Car(Vehicle):
    trunk_open = False
    def open_trunk(self):
        self.trunk_open = True
    def close_trunk(self):
        self.trunk_open = False

# Overriding Python method __init__
class Motorcycle(Vehicle):
    def __init__(self, center_stand_out = False):
        self.center_stand_out = center_stand_out
        super().__init__()
    # Overriding other methods
    def start(self):
        print("Sorry, out of fuel!")

car = Car()
car.start()
motorcycle = Motorcycle()
motorcycle.start()