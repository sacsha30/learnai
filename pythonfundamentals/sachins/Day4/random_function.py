from random import *
random_number = randint(1,10)
print(random_number)

#2
#from random import *
random_number = uniform(0.0,1.0) #float value
print(random_number)

#3
#from random import *
names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
raffle = choice(names)
print(raffle)
