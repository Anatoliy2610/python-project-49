import random
import math


GAME_GCD = 'Find the greatest common divisor of given numbers.'


def get_nums_pair_and_gcd():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    question = f'{a} {b}'
    result = math.gcd(a, b)
    return question, str(result)
