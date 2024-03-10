from random import randint
from math import gcd
import prompt

def game_gcd():
    name = prompt.string('May I have you name? ')
    if  len(name) <= 0:
        name = input()
    else:
        print ('Hello, ' + name + '!')

    print ('Find the greatest common divisor of given numbers.')

    i = 1
    while i <= 3:
        a = randint (1, 25)
        b = randint (1,25)
        print ('Questiom: ' + str(a) + ' ' + str(b))
        
        user_answer = prompt.string('Your answer: ')

        result = gcd(a, b)
        
        if user_answer == str(result):
            print ('Correct!')
            i += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{result}'")
            print ("Let's try again, " + name + "!")
            i = 1
    print ('Congratulations, ' + name + '!')




