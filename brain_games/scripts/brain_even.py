#!/usr/bin/env python3
from brain_games.games.even import get_num_is_even, GAME_EVEN
from brain_games.engin import get_run_brain_game


def run_even_game():
    get_run_brain_game(get_num_is_even, GAME_EVEN)


def main():
    run_even_game()


if __name__ == '__main__':
    main()
