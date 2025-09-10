list_names = ["Steven", "Jackie", "Donna", "Kelso", "Eric", "Fez", "Kitty", "Red"]
for index, name in enumerate(list_names):
    print(f'{name} is found at index {index}')

#2 Print indices of all the characters in a string
indices_list = []
for index, item in list(enumerate("Python")):
    indices_list.append(index)

print(indices_list)

#3 Print indices of all the words start with M
list_names = ["Maverick", "Alice", "Madeline", "Hazel", "Jack", "Meadow", "Thomas", "Emily", "Mills"]
for index, item in enumerate(list_names):
    if item.startswith('M'):
        print(index)