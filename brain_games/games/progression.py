from random import randint


GAME_RULE = 'What number is missing in the progression?'


def take_task_and_answer():
    step = randint(1, 5)
    len_series = randint(5, 10)
    random_index = randint(0, len_series)
    progression = list(range(1, 100, step))
    series = progression[:len_series]
    correct_answer = str(series[random_index - 1])
    series[random_index - 1] = '..'
    series_str = [str(a) for a in series]
    random_number = (" ".join(series_str))
    return random_number, correct_answer
