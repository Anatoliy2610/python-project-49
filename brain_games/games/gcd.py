import random
import math
from brain_games.engin import get_run_games
from brain_games.engin import game_gcd


def get_nums_pair_and_gcd():
    a = random.randint(1, 25)
    b = random.randint(1, 25)
    question = f'{a} {b}'
    result = math.gcd(a, b)
    return question, str(result)


def run_gcd_game():
    get_run_games(get_nums_pair_and_gcd, game_gcd)
