input1 = input("Enter a string")
input2 = input("Enter first character")
input3 = input("Enter second character")
input4 = input("Enter third character")

input1_list = input1.split(" ")
total_words = len(input1_list)
print(f"Total words: {total_words}")
first_letter = input1_list[0]
last_letter = input1_list[-1]
print(f"first and last letter of list is {first_letter} and {last_letter}")

input1_list.reverse()
print(f"inverted list: {input1_list}")

contains_python = "python" in input1_list
print(f"Word python exits in list: {contains_python}")

