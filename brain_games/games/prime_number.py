from random import randint
import math


RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def take_task_and_answer():
    question = randint(2, 100)
    correct_answer = "yes" if is_prime(question) else "no"
    return question, correct_answer


def is_prime(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True
