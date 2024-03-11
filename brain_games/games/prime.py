from random import randint, choice
import prompt



def prime():
    name = prompt.string('May I have you name? ')
    if  len(name) <= 0:
        name = input()
    else:
        print ('Hello, ' + name + '!')

    print ('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 1

    while i <= 3:
        number = randint(1,100)
        print ('Question: ' + str(number))
        
        result = []
        n = 1
        while n <= 100:
            if number % n == 0:
                result.append(n)
                n += 1
            else:
                n += 1

        if len(result) == 2:
            answer = 'yes'
        else:
            answer = 'no'

        answer_user = prompt.string('Your answer: ')

        if answer == answer_user:
            print ('Correct!')
            i += 1
        else:
            print(f"'{answer_user}' is wrong answer ;(. Correct answer was '{answer}'")
            print ("Les's try again, " + name + "!")
            i = 1
    print ('Congratulations, ' + name + '!')
