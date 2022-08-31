from random import randint, choice


RULE = 'What is the result of the expression?'


def take_task_and_answer():
    rand_num1 = randint(1, 20)
    rand_num2 = randint(1, 20)
    operator = choice('+-*')
    question = (f'{rand_num1} {operator} {rand_num2}')
    if operator == '+':
        correct_answer = rand_num1 + rand_num2
    elif operator == '-':
        correct_answer = rand_num1 - rand_num2
    elif operator == '*':
        correct_answer = rand_num1 * rand_num2
    return question, str(correct_answer)
