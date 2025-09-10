#1
students = ["Norville", "Fred", "Velma", "Daphne"]
for item in students:
    print("Hello", item)

#2
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_numbers = 0
for item in list_numbers:
    sum_numbers = sum_numbers + item
#3
list_numbers = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
sum_even = 0
sum_odd = 0

for item in list_numbers:
    if item % 2 == 0 :
        sum_even = sum_even + item
    elif item % 2 != 0 :
        sum_odd = sum_odd + item