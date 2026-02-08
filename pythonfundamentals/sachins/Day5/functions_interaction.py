"The sum of your dice is {suma_dados}. Unfortunate"
"The sum of your dice is {suma_dados}. You have a good chance"
"The sum of your dice is {sum_dice}. It looks like a winning roll"
from random import randint


def throw_dice():
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    print(num1, num2)
    return (num1, num2)


def roll_result(num1, num2):
    msg = ''
    sum_dice = num1 + num2
    if sum_dice <= 6:
        msg = "The sum of your dice is " + str(sum_dice) + ". Unfortunate"
    elif 6 < sum_dice < 10:
        msg = "The sum of your dice is " + str(sum_dice) + ". You have a good chance"
    elif sum_dice >= 10:
        msg = "The sum of your dice is " + str(sum_dice) + ". It looks like a winning roll"
    return msg
(num1, num2) = throw_dice()
roll_result(num1, num2)