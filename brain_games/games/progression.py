from random import randint


GAME_RULES = 'What number is missing in the progression?'


def series_str():
    step = randint(1, 5)
    len_series = randint(5, 10)
    change_numb = randint(0, len_series)
    progress = list(range(1, 100, step))
    series = progress[:len_series]
    global answer
    answer = str(series[change_numb - 1])
    series[change_numb - 1] = '..'
    series_str = [str(a) for a in series]
    return (" ".join(series_str))


def progression():
    task = series_str()
    correct_answer = str(answer)
    return task, correct_answer
