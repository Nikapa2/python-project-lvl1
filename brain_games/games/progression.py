from random import randint


GAME_RULE = 'What number is missing in the progression?'


def series_str():
    step = randint(1, 5)
    len_series = randint(5, 10)
    random_index = randint(0, len_series)
    progression = list(range(1, 100, step))
    series = progression[:len_series]
    answer = str(series[random_index - 1])
    series[random_index - 1] = '..'
    series_str = [str(a) for a in series]
    return (" ".join(series_str)), answer


def take_task_and_answer():
    task, answer = series_str()
    correct_answer = answer
    return task, correct_answer
