import random


GAME_PROGRESSION = 'What number is missing in the progression?'


def get_progression():
    num = random.randint(0, 10)
    step = random.randint(2, 6)
    len_progression = 10
    progr = []
    for next_num in range(len_progression):
        progr_step = num + next_num * step
        progr.append(progr_step)
    return progr


def get_progression_nums():
    result = get_progression()
    result_copy = result.copy()
    number_answer_progression = random.randint(0, len(result) - 1)
    result[number_answer_progression] = '..'
    string_result = ' '.join(str(i) for i in result)
    answer = result_copy[number_answer_progression]
    return string_result, str(answer)
