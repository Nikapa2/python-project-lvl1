from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def take_task_and_answer():
    task = randint(2, 100)
    correct_answer = "yes" if is_prime(task) else "no"
    return task, correct_answer


def is_prime(task):
    for i in range(2, int(task / 2) + 1):
        if task % i == 0 or task == 1 or task == 0:
            return False
    else:
        return True
