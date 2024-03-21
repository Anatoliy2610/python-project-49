import random


def get_num_and_prime_ans():
    max_num = 100
    num = random.randint(1, max_num)
    result = []
    divider = 1
    while divider <= max_num:
        if num % divider == 0:
            result.append(divider)
            divider += 1
        else:
            divider += 1
    if len(result) == 2:
        answer = 'yes'
        return str(num), answer
    else:
        answer = 'no'
        return str(num), answer
