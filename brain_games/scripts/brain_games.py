#!/usr/bin/env python3


def hello():
    print('WeloME to the Brain Games!')
    from brain_games.games.cli import welcome_user
    welcome_user('')


def main():
    hello()


if __name__ == '__main__':
    main()
