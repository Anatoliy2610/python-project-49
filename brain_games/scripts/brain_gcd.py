#!/usr/bin/env python3
from brain_games.games.gcd import get_nums_pair_and_gcd, GAME_GCD
from brain_games.engin import get_run_brain_game


def run_gcd_game():
    get_run_brain_game(get_nums_pair_and_gcd, GAME_GCD)


def main():
    run_gcd_game()


if __name__ == '__main__':
    main()
