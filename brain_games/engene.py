import prompt


WIN_SCORE = 3


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, ,{name}!')
    return name


def engine(game): # game:name game modul.
    name = welcome_user()
    print(game.GAME_RULES)
    for i in range(WIN_SCORE):
        correct_answer, task = game.process_of_game()
        print(f"Question: {task}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
            continue
        fail_answer(name, correct_answer, user_answer)
        break
    else:
        print(f'Congratulations, {name}!')


def fail_answer(name, correct_answer, user_answer):
    name = welcome_user()
    print(f"{user_answer} is wrong answer ;(. Correct answer was {correct_answer}")
    print(f"Let\'s try again, {name}!")
