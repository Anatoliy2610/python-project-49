import random


GAME_PRIME = 'Answer "yes" if given number is prime. Otherwise answer "no".'
MIN_NUMBER = 1
MAX_NUMBER = 100


def is_prime(num):
    result = []
    divider = 1
    while divider <= MAX_NUMBER:
        if num % divider == 0:
            result.append(divider)
            divider += 1
        else:
            divider += 1
    return len(result) == 2


def get_num_and_prime_ans():
    num = random.randint(MIN_NUMBER, MAX_NUMBER)
    result_answer = 'yes' if is_prime(num) else 'no'
    return num, result_answer
