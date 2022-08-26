from random import randint


GAME_RULE = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def take_task_and_answer():
    random_number = randint(2, 100)
    correct_answer = "yes" if is_prime(random_number) else "no"
    return random_number, correct_answer


def is_prime(number):
    for i in range(2, int(number / 2) + 1):
        if number % i == 0 or number < 2:
            return False
    else:
        return True
