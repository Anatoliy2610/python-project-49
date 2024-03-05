#!/usr/bin/env python3


def hello():
    print('Welome to the Brain Games!')
    from brain_games.cli import welcome_user
    welcome_user('')


def main():
    hello()


if __name__ == '__main__':
    main()
