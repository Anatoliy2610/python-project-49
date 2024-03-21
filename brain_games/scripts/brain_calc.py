#!/usr/bin/env python3
from brain_games.engin import get_run_games
from brain_games.CONSTANT import GAME_CALC
from brain_games.games import get_math_expression_and_result


def run_calc_game():
    get_run_games(get_math_expression_and_result, GAME_CALC)


def main():
    run_calc_game()


if __name__ == '__main__':
    main()
