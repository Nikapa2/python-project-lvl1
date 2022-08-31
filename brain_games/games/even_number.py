from random import randint


RULE = 'Answer "yes" if the number is even, otherwise answer "no".'


def take_task_and_answer():
    question = randint(1, 100)
    correct_answer = "yes" if question % 2 == 0 else "no"
    return question, correct_answer
