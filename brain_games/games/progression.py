import random
from brain_games.engin import game_progression
from brain_games.engin import get_run_games


def get_progression_nums():
    num = random.randint(0,10)
    step = random.randint(2,6)
    len_progression = 10
    result = []
    next_num = 0
    while next_num < len_progression:
        result_sum = num + next_num * step
        result.append(result_sum)
        next_num+=1
        
    number_answer = random.randint(0, len(result)-1)
    result_copy = result.copy()
    result[number_answer] = '..'
    string_result = ' '.join(str(i) for i in result)
    answer = result_copy[number_answer]
    return string_result, str(answer)

def run_progression_game():
    get_run_games(get_progression_nums, game_progression)
