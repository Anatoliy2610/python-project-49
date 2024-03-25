import random


GAME_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_num_is_even():
    num = random.randint(1, 25)
    result = 'yes' if is_even(num) else 'no'
    return num, result
