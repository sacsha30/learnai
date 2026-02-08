"""Create a function called return_distincts() that receives 3
integers as parameters.
If the sum of the 3 numbers is greater than 15, it must return
the highest number.
If the sum of the 3 numbers is less than 10, it must return the
lowest number.
If the sum of the 3 numbers is a value between 10 and 15
(included), then it must return the number with the
intermediate value."""

def return_distincts(num1, num2, num3):
    sum_numbers = sum([num1, num2, num3])
    greatest = max(num1, num2, num3)
    lowest = min(num1, num2, num3)

    if sum_numbers > 15:
        return greatest
    elif sum_numbers < 10:
        return lowest
    elif 10 < sum_numbers < 15:
        return sum_numbers

print(return_distincts(10,1,3))
