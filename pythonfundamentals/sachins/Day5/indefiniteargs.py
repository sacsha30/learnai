#exercise 1
def number_attributes(**kwargs):
    count = 0
    for key, value in kwargs.items():
        count += 1

    return count


print(number_attributes(x=1, y=2))

#exercise 2
def list_attributes(**kwargs):
    list_attr = []
    for key, value in kwargs.items():
        list_attr.append(value)

    return list_attr


print(list_attributes(x=1, y=2))