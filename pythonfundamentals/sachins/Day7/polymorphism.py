#
a_word = "polymorphism"
a_list = ["Classes", "OOP", "Polymorphism"]
a_tuple = (1, 2, 3, 80)

def iter_list(lst):
    return len(lst)

print(iter_list(a_word))
print(iter_list(a_list))
print(iter_list(a_tuple))

#
class Wizard():
    def attack(self):
        print("magic attack")

class Archer():
    def attack(self):
        print("shoot arrow")

class Samurai():
    def attack(self):
        print("katana attack")

wizard = Wizard()
archer = Archer()
samurai = Samurai()
characters = [archer, wizard, samurai]

for character in characters:
    character.attack()

#
class Wizard():
    def defend(self):
        print("magic shield")

class Archer():
    def defend(self):
        print("duck")

class Samurai():
    def defend(self):
        print("block")

def general_defense(character):
    character.defend()

