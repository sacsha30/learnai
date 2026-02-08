from random import choice

secret_codes = [1, 2, 3, 4, 5, 6]


def toss_coin():
    return choice(["Heads", "Tails"])


def luck(result, secret_codes):
    if result == "Tails":
        print("List will self-destruct")
        return []
    else:
        print("List was saved")
        return secret_codes


luck(toss_coin(), secret_codes)


