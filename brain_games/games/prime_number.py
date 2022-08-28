from random import randint
import math


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def take_task_and_answer():
    random_number = randint(2, 100)
    correct_answer = "yes" if is_prime(random_number) else "no"
    return random_number, correct_answer


def is_prime(number):
    if number >= 2:
        for i in range(2, int(math.sqrt(number) + 1)):
            if number % i == 0:
                return False
        else:
            return True
    return False
