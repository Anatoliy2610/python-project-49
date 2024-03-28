import random
import math


GAME_GCD = 'Find the greatest common divisor of given numbers.'
MIN_NUMBER = 1
MAX_NUMBER = 25


def get_nums_pair_and_gcd():
    a = random.randint(MIN_NUMBER, MAX_NUMBER)
    b = random.randint(MIN_NUMBER, MAX_NUMBER)
    question = f'{a} {b}'
    result = math.gcd(a, b)
    return question, str(result)
