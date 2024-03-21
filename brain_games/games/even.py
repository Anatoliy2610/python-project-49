import random


def get_num_is_even():
    num = random.randint(1, 25)
    if num % 2 == 0:
        return num, 'yes'
    else:
        return num, 'no'


def run_even_game():
    get_run_games(get_num_is_even, GAME_EVEN)
