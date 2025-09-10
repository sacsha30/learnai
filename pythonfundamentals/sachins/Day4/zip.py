#1
capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]
for capital, country in list(zip(capitals, countries)):
    print(f"The capital of {country} is {capital}")

#2
brands = ['Nike', 'Adidas', 'Sketchers', 'Asics']
products = ['Running Shoe', 'T-Shirt', 'Casual Shoes', 'Tennis Shoe']
my_zip = zip(brands, products)

#3
spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]
numbers = list(zip(spanish, portuguese, english))