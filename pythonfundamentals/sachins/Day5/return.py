def power(num1, num2):
    return num1 ** num2


def usd_to_eur(num):
    return num * 0.9
dollars = 100
usd_to_eur(dollars)


def reverse_word(chars):
    reverse_str = chars[::-1].upper()
    return reverse_str
word = "Sachin"
reverse_word(word)


def all_positives(nlist):
    positive_list = []
    for num in nlist:
        if num < 0:
            return False
        else:
            pass
    return True
numbers = [1, 2, 1]
print(all_positives(numbers))

def sum_less(nlist):
    nsum = 0
    for n in nlist:
        if n > 0 and n < 1000:
            nsum += n
        else:
            pass
    return nsum
numbers = [1,2,3]
print(sum_less(numbers))

def count_even(nlist):
    neven = [n for n in nlist if n % 2 ==0]
    return len(neven)
numbers = [2,4,5,6,7]
count_even(numbers)
