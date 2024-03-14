import prompt


def welcome_user():
    name = prompt.string('May I have your name? ')

    if len(name) <= 0:
        name = input()

    else:
        print('Hello, ' + name + '!')
