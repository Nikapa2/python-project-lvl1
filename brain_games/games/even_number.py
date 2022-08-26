from random import randint


GAME_RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def take_task_and_answer():
    random_number = randint(1, 100)
    correct_answer = "yes" if random_number % 2 == 0 else "no"
    return random_number, correct_answer
