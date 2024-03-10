from random import randint, choice
from operator import add, sub, mul
import prompt



def calc():
    name = prompt.string('May I have you name? ')
    if  len(name) <= 0:
        name = input()
    else:
        print ('Hello, ' + name + '!')

    print ('What is the result of the expression?')
    i = 1

    while i <= 3:
        numb1 = randint(1,10)
        numb2 = randint(1,10)
        sign = choice ('+-*')
        print ('Question: ' + str(numb1) + str(sign) + str(numb2))
        if sign == '+':
            result = add(numb1, numb2)

        if sign == '-':
            result = sub(numb1, numb2)
        
        if sign == '*':
            result = mul(numb1, numb2)

        answer_user = prompt.string('Your answer: ')
        
        if str(result) == answer_user:
            print ('Correct!')
            i += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{result}'")
            print ("Les's try again, " + name + "!")
            i = 1
    print ('Congratulations, ' + name + '!')



