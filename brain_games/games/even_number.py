from random import randint


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def process_of_game():
    task = randint(1, 100)
    correct_answer = "yes" if task % 2 == 0 else "no"
    return task, correct_answer
