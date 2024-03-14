#!/usr/bin/env python3

from brain_games.cli import welcome_user

def hello():
    print('Welcome to the brain-games!')
    welcome_user()


def main():
    hello()


if __name__ == '__main__':
    main()
