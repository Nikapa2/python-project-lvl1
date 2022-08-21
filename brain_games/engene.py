import prompt


WIN_SCORE = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def engine(game):  # game:name game modul.
    name = welcome_user()
    print(game.GAME_RULES)
    for i in range(WIN_SCORE):
        task, correct_answer = game.process_of_game()
        print("Question: {}".format(task))
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
            continue
        fail_answer(name, correct_answer, user_answer)
        break
    else:
        print(f'Congratulations, {name}!')


def fail_answer(name, correct_answer, user_answer):
    print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))  # noqa: E501
    print("Let's try again, {0}!".format(name))
