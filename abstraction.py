from abc import ABC
class Vehicle(ABC):
    def start_engine(self):
        pass
class Car(Vehicle):
    def start_engine(self):
        print("Car engine started")
class Bike(Vehicle):
    def start_engine(self):
        print("Bike engine started")
class Bus(Vehicle):
    def start_engine(self):
        print("Bike engine started")
c=Car()
b=Bike()
bs=Bus()
c.start_engine()
b.start_engine()
bs.start_engine()