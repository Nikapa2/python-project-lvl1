from random import randint, choice


GAME_RULES = 'What is the result of the expression?'


def calc():
    rand_num1 = randint(1, 20)
    rand_num2 = randint(1, 20)
    operator = choice('+-*')
    task = '{rand_num1}{operator}{rand_num2}'
    correct_answer = str(eval(f'{rand_num1}{operator}{rand_num2}'))
    return task, correct_answer