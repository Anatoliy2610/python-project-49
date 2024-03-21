#!/usr/bin/env python3
from brain_games.games.prime import get_num_and_prime_ans
from brain_games.engin import get_run_games
from brain_games.CONSTANT import GAME_PRIME

def run_prime_game():
    get_run_games(get_num_and_prime_ans, GAME_PRIME)


def main():
    run_prime_game()


if __name__ == '__main__':
    main()
