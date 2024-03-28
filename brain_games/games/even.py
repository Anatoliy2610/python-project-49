import random


GAME_EVEN = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 25


def is_even(num):
    return num % 2 == 0


def get_num_is_even():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    result = 'yes' if is_even(num) else 'no'
    return num, result
