from random import choice
import sys

choices = ["sachin","sharma"]
result = ""
lives_remaining = 5
hangman = choice(choices)
lst_hangman = list(hangman)
for n in hangman:
    result += "*"
print(result)

while result != hangman or lives_remaining != 0:
    user_choice = input("Enter an alphabet: ")

    if user_choice in hangman:
        lst_result = list(result)
        count = 0
        for item in lst_hangman:
            if user_choice == item:
                lst_result[count] = item
            count += 1
        result = "".join(lst_result)
        print(result)
    else:
        lives_remaining -= 1
        for n in hangman:
            lst_result = list(result)
        if lives_remaining == 0:
            print("You lose!")
            sys.exit(1)
        else:
            print(f"lives remaining: {lives_remaining}")

    if result == hangman:
        print("You win!")
        sys.exit(1)

