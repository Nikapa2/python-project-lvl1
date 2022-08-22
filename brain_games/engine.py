import prompt


NUMBER_OF_ROUNDS = 3


def engine(game):  # game:name game modul.
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULES)
    for _ in range(NUMBER_OF_ROUNDS):
        task, correct_answer = game.process_of_game()
        print("Question: {}".format(task))
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
            continue
        print("'{0}' is wrong answer ;(. Correct answer was '{1}'.".format(user_answer, correct_answer))  # noqa: E501
        print("Let's try again, {0}!".format(name))
        break
    else:
        print(f'Congratulations, {name}!')
