import random
import math


def get_nums_pair_and_gcd():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    question = f'{a} {b}'
    result = math.gcd(a, b)
    return question, str(result)
