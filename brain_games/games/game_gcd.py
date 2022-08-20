from random import randint
from math import gcd


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def process_of_game():
    rand_num1 = randint(1, 100)
    rand_num2 = randint(1, 100)
    task = '{rand_num1} {rand_num2}'
    correct_answer = str(gcd(rand_num1, rand_num2))
    return task, correct_answer
