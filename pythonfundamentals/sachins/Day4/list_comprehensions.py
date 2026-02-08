values = [1, 2, 3, 4, 5, 6, 9.5]
square_values = [value ** 2 for value in values]

values = [1, 2, 3, 4, 5, 6, 9.5]
even_values = [n for n in values if n %2 == 0]
print(even_values)

temperature_fahrenheit = [32, 212, 275]
degrees_celsius = [(n-32)*(5/9) for n in temperature_fahrenheit]