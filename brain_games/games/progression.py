from random import randint, choice
from operator import add, sub, mul
import prompt



def progression():
    name = prompt.string('May I have you name? ')
    if  len(name) <= 0:
        name = input()
    else:
        print ('Hello, ' + name + '!')

    print ('What number is missing in the progression?')
    
    i = 1
    while i <= 3:
        numb1 = randint(0,10)
        step = randint(2,6)
        last_number = numb1 + step * 10
        
        result = []
        m = 0
        while m <= 9:
            result_sum = numb1 + m * step
            result.append(result_sum)
            m+=1
        
        random_number = randint(0, len(result)-1)
        result_copy = result.copy()

        result[random_number] = '..'

        n = 0
        result_question = ''
        while n < len(result):
            result_question = result_question + ' ' + str(result[n])
            n += 1


        print ('Question: ' + result_question.strip())

        answer_user = prompt.string('Your answer: ')

        if str(result_copy[random_number]) == answer_user:
            print ('Correct!')
            i += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{result_copy[random_number]}'")
            print ("Les's try again, " + name + "!")
            i = 1
    print ('Congratulations, ' + name + '!')





