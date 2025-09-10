num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num2 > num1:
    print(f"{num2} is greater than {num1}")
else:
    print(f"{num1} and {num2} are equal")


age = 16
has_license = False

if age > 18 and has_license == True:
    print("You can drive")
elif age < 18:
    print("You can't drive yet. You must be 18 years old and have a license")
elif has_license == False:
    print("You can't drive. You need to have a license")


speak_french = True
knows_python = False

if speak_french == True and knows_python == True:
    print("You meet the requirements to app")
elif speak_french == False and knows_python == False:
    print("To apply, you need to know how to program in Python and speak French")
elif speak_french == False:
    print("To apply, you need to speak French")
elif knows_python == False:
    print("To apply, you need to know how to program in Python")