import random
import operator


GAME_CALC = 'What is the result of the expression?'
MIN_NUMBER = 1
MAX_NUMBER = 10


def get_math_expression_and_result():
    num1 = random.randint(MIN_NUMBER, MAX_NUMBER)
    num2 = random.randint(MIN_NUMBER, MAX_NUMBER)
    sign = random.choice('+-*')
    question = f'{num1} {sign} {num2}'
    if sign == '+':
        right_answer = operator.add(num1, num2)
    if sign == '-':
        right_answer = operator.sub(num1, num2)
    if sign == '*':
        right_answer = operator.mul(num1, num2)
    return question, str(right_answer)
