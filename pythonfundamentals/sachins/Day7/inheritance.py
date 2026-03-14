#Create a class called Person, which has the following instance attributes: name, age. Create another class,
# Student, which inherits these attributes from the first.
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    pass

#Create a class called Pet, which has the following instance attributes: age, name, legs.
# Create another class, Dog, which inherits its attributes from the first.
class Pet:

    def __init__(self, age, name, legs):
        self.age = age
        self.name = name
        self.legs = legs

class Dog(Pet):
    pass

#zCreate a class called Vehicle, which contains the speed() and slow_down() methods
# (you can leave the method code blank with pass). Create a class called Car that inherits these methods from Vehicle.
class Vehicle:

    def speed(self):
        pass

    def slow_down(self):
        pass

class Car(Vehicle):
    pass

#to see method resolution order
print(Car.__mro__)

#If the Daughter class has inherited her way of laughing from her father, and her vocation from her mother,
# and today they have the same job at the Prosecutor's Office, create multiple inheritance that allows
# this class to inherit correctly from Father and Mother.
class Father():
    def work(self):
        print("Working in the Public Hospital")

    def laugh(self):
        print("Ha Ha Ha!")

class Mother():
    def work(self):
        print("Working in the Public Prosecutor's Office")

class Daughter(Mother, Father):
    pass

#"The platypus is one of the rarest creatures in the world: although it is a mammal, it lays eggs; and it nurses
# its young but has no nipples." (National Geographic)
#Create a Platypus class that inherits from other classes: Vertebrate, Fish, Reptile, Bird, and Mammal, so that you "build" an animal that has the following methods and attributes:
# - lay_eggs()
# - has_peak = True
# - vertebrate = True
# - poisonous = True
# - swim()
# - walk()
# - nurse()
class Vertebrate:
    vertebrate = True

class Bird(Vertebrate):
    has_peak = True
    def lay_eggs(self):
        print("laying eggs")

class Reptile(Vertebrate):
    poisonous = True

class Fish(Vertebrate):
    def swim(self):
        print("swimming")
    def lay_eggs(self):
        print("laying eggs")

class Mammal(Vertebrate):
    def walk(self):
        print("walking")
    def nurse(self):
        print("nursing pups")

class Platypus(Fish, Reptile, Bird, Mammal):
    pass

#A son has inherited all his characteristics from his father, however, they have different hobbies.
# Make the Child class inherit all its methods and attributes from Father,
# overriding the hobby() method so that it returns [1]: "I play video games in my free time"
class Father():
    eye_color = "brown"
    hair = "curly"
    height = "average"
    voice = "deep"
    favorite_sport = "tennis"

    def laugh(self):
        return "LOL"

    def hobby(self):
        return "I work with wood in my free time"

    def walk(self):
        return "Walking with long and quick steps"

class Child(Father):
    def hobby(self):
        return "I play video games in my free time"