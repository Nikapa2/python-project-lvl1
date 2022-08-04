from random import randint
import prompt


def even_number():
    name = prompt.string('May I have your name? ')
    print(f'Hello, ,{name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    win_answer = 3

    while count < win_answer:
        random_number = randint(1, 100)
        odd_num = random_number % 2 != 0
        even_num = random_number % 2 == 0
        print(f"Question: {random_number}")
        user_answer = prompt.string("Your answer: ")
        if even_num and user_answer.lower() == "yes" or odd_num and user_answer.lower() == "no":
            print('Correct!')
            count += 1
        elif odd_num and user_answer.lower() == "yes":
            return print(f'"yes" is wrong answer ;(. Correct answer was "no"\nLet\'s try again, {name}')
        elif even_num and user_answer.lower() == "no":
            return print(f'"no" is wrong answer ;(. Correct answer was "yes"\nLet\'s try again, {name}')
    print(f'Congratulations, {name}!')
