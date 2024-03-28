import random


GAME_PROGRESSION = 'What number is missing in the progression?'
MIN_NUMBER = 0
MAX_NUMBER = 10
MIN_COMMON_DIFF = 2
MAX_COMMON_DIFF = 10
LEN_ARITHMETIC_PROGRESSION = 10


def get_progression(initial_num, common_difference):
    arithmetic_progression = []
    for next_num in range(LEN_ARITHMETIC_PROGRESSION):
        arithmetic_series = initial_num + next_num * common_difference
        arithmetic_progression.append(arithmetic_series)
    return arithmetic_progression


def get_progression_nums():
    initial_num = random.randint(MIN_NUMBER, MIN_NUMBER)
    common_diff = random.randint(MIN_COMMON_DIFF, MAX_COMMON_DIFF)
    result = get_progression(initial_num, common_diff)
    result_copy = result.copy()
    hidden_number_progression = random.randint(MIN_NUMBER, len(result) - 1)
    result[hidden_number_progression] = '..'
    string_result = ' '.join(str(i) for i in result)
    right_answer = result_copy[hidden_number_progression]
    return string_result, str(right_answer)
