import random
import operator
from brain_games.engin import get_run_games
from brain_games.engin import game_calc


def get_math_expression_and_result():
    numb1 = random.randint(1, 10)
    numb2 = random.randint(1, 10)
    sign = random.choice('+-*')
    question = str(numb1) + str(sign) + str(numb2)
    if sign == '+':
        answer = operator.add(numb1, numb2)
    if sign == '-':
        answer = operator.sub(numb1, numb2)
    if sign == '*':
        answer = operator.mul(numb1, numb2)
    return question, str(answer)


def run_calc_game():
    get_run_games(get_math_expression_and_result, game_calc)
