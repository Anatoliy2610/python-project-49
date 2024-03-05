from random import randint
from brain_games.cli import welcome_user
import prompt


def yes_or_no():
    name = prompt.string('May I have you name? ')
    if  len(name) <= 0:
        name = input()
    else:
        print ('Hello, ' + name + '!')

    print ('Answer "yes" if the numbers is even, otherwise answer "no"')
    i = 1
    while i <= 3:
        numb = randint (1, 25)
        print ('Question: ' + str (numb))
        answer = prompt.string('Your answer: ')

        if numb % 2 == 0:
            result = 'yes'
        else:
            result = 'no'

        if answer == result:
            print ('Correct!')
            i += 1

        else:
            print (f"'{answer}' is wrong answer ;(. Correct answer was '{result}'")
            print ("Let's try again, " + name + "!")
            i = 1
    print('Congratulations, ' + name + '!')
