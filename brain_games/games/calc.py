import random
import operator


def get_math_expression_and_result():
    numb1 = random.randint(1, 10)
    numb2 = random.randint(1, 10)
    sign = random.choice('+-*')
    question = f'{numb1} {sign} {numb2}'
    if sign == '+':
        answer = operator.add(numb1, numb2)
    if sign == '-':
        answer = operator.sub(numb1, numb2)
    if sign == '*':
        answer = operator.mul(numb1, numb2)
    else:
        break
    return question, str(answer)

