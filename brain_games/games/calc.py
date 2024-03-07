from random import randint, choice
from operator import add, sub, mul
import prompt



def calc():
    print ('What is the result of the expresSION?')
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
            print ("Les's try again, " + 'Oleg' + "!")
            i = 1
    print ('Congratulations, ' + 'Oleg' + '!')



