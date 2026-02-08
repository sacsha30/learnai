my_set_1 = {1, 2, "three", "four"}
my_set_2 = {"three", 4, 5}
my_set_3 = my_set_1.union(my_set_2) #join two sets

raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
item = raffle.pop() #remove random element

raffle = {"Rachel", "Monica", "Phoebe", "Joey", "Chandler", "Ross"}
raffle.add("Gunther") #add an element to set
print(raffle)