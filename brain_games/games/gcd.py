from random import randint
from math import gcd


RULE = 'Find the greatest common divisor of given numbers.'


def take_task_and_answer():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    question = '{0} {1}'.format(rand_num1, rand_num2)
    correct_answer = str(gcd(rand_num1, rand_num2))
    return question, correct_answer
