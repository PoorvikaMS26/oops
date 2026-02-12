from abc import ABC, abstractmethod 
class Animal(ABC): 
    @abstractmethod 
    def sound(self): 
        pass   
    def sleep(self): 
        print("This animal is sleeping") 
class Dog(Animal): 
    def sound(self): 
        print("Dog says: Bark") 
class Cat(Animal): 
    def sound(self): 
        print("Cat says: Meow") 
class Cow(Animal): 
    def sound(self): 
        print("Cow says: Moo") 
d = Dog() 
c = Cat() 
co = Cow() 
d.sound() 
d.sleep() 
c.sound() 
c.sleep() 