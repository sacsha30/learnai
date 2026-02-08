numbers = [1, 2, 15, 7, 2]


def reduce_list(numbers):
    unique_values = set(numbers)
    max_number = max(unique_values)
    unique_values_list = list(unique_values)
    unique_values_list.remove(max_number)
    return unique_values_list


def average(numbers):
    return sum(numbers) / len(numbers)


average(reduce_list(numbers))