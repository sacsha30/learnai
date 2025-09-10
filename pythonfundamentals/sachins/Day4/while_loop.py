#1
number = 10
while number != -1:
    print(number)
    number -= 1

#2
number = 50
while number >= 0:
    if number % 5 == 0:
        print(number)
        number -= 1
    else:
        number -= 1
        continue

