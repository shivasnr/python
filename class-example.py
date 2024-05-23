class Car:
    speed = 0
    started = False
    def start(self):
        self.started = True
        print("Car started, let's ride!")
    def increase_speed(self, delta):
        if self.started:
            self.speed = self.speed + delta
            print('Vrooooom!')
        else:
            print("You need to start the car first")
    def stop(self):
        self.speed = 0
        print('Halting')
# car = Car()
# car.increase_speed(10)
# car.start()
# car.increase_speed(40)
# car.stop()
car1 = Car()
car2 = Car()
car1.start()
car1.speed = 10
print('Car 1 speed: ', car1.speed)
print('Car 2 Speed: ', car2.speed)
