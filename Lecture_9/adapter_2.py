import random

class Car:
    def accelerate(self):
        print("Speed after accelerating:", random.Random().randint(100, 140))
        
    def apply_brakes(self):
        print("Speed after brake pedal:", random.Random().randint(20, 40))

    def assign_driver(self, name):
        print("The driver's name is:", name)

class Motorbike:
    def rev(self):
        print("\nSpeed after revving:", random.Random().randint(100, 140))

    def pull_brake_lever(self):
        print("Speed after brake lever:", random.Random().randint(20, 40))

    def assign_rider(self, name):
        print("The driver's name is:", name)


class CarAdapter:
    def __init__(self):
        self.car = Car()
        
    def speedUp(self):
        self.car.accelerate()
        
    def brake(self):
        self.car.apply_brakes()
        
    def assign(self, name):
        self.car.assign_driver(name)


class MotorbikeAdapter:
    def __init__(self):
        self.vehicleMotorbike = Motorbike()
        
    def speedUp(self):
        self.vehicleMotorbike.rev()
        
    def brake(self):
        self.vehicleMotorbike.pull_brake_lever()
        
    def assign(self, name):
        self.vehicleMotorbike.assign_rider(name)
        

def main():
    vehicles = [CarAdapter(), MotorbikeAdapter()]

    for i in vehicles:
        i.speedUp()
        i.brake()
        i.assign("John Pork")

main()