import prompt


NUMBER_OF_ROUNDS = 3


def run(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(game.GAME_RULE)
    for _ in range(NUMBER_OF_ROUNDS):
        random_number, correct_answer = game.take_task_and_answer()
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print('Correct!')
            continue
        print(
            f"{user_answer} is wrong answer ;(. "
            f"Correct answer was {correct_answer}."
        )
        print(f"Let's try again, {name}!")
        break
    else:
        print(f'Congratulations, {name}!')
