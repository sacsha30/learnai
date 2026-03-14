class Character:
    pass
harry_potter = Character()

#instance attributes
class House:

    def __init__(self, color, floors):
        self.color = color
        self.floors = floors

white_house = House('white', 4)

#class attributes
class Cube:
    sides = 6

    def __init__(self, color):
        self.color = color

red_cube = Cube('red')

#
class Character:
    real = False

    def __init__(self, species, magical, age):
        self.species = species
        self.magical = magical
        self.age = age

harry_potter = Character('Human', True, 17)

#class methods
class Dog:
    def bark(self):
        print('Woof!')

d = Dog()
d.bark()

#class methods 2
class Wizard:
    def cast_spell(self):
        print("Abracadabra!")

merlin = Wizard()
merlin.cast_spell()

#class methods 3
class Alarm:
    def snooze(self, minutes):
        print(f'The alarm has been postponed {minutes} minutes')

i_alarm = Alarm()
i_alarm.snooze(15)

#static methods
class Pet:
    @staticmethod
    def breathe():
        print("Inhale... Exhale")

Pet.breathe()

#class methods
class Player:
    alive = False

    @classmethod
    def revive(cls):
        cls.alive = True
        print(Player.alive)

#Create an instance method throw_arrow() that subtracts by -1 the number of arrows a Character instance has, which in
# turn has an instance attribute called arrows_amount (that stores a certain number).
class Character:

    def __init__(self, arrows_amount):
        self.arrows_amount = arrows_amount

    def throw_arrow(self):
        self.arrows_amount -= 1

#check the parent class
print(Character.__bases__)

#check the subclasses
print(Character.__subclasses__())