#!/usr/bin/env python3
from brain_games.games.progression import get_progression_nums
from brain_games.CONSTANT import GAME_PROGRESSION
from brain_games.engin import get_run_games


def run_progression_game():
    get_run_games(get_progression_nums, GAME_PROGRESSION)


def main():
    run_progression_game()


if __name__ == '__main__':
    main()
