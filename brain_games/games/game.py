from random import randint, choice
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, ,{name}!')
    return name
    
def even_number():
    name = welcome_user()
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

def calc():

    name = welcome_user()
    print('What is the result of the expression?')
    count = 0
    win_answer = 3
    while count < win_answer:
        rand_num1 = randint(1, 20)
        rand_num2 = randint(1, 20)
        operator = choice('+-*')
        answer = str(eval(f'{rand_num1}{operator}{rand_num2}'))
        print(f"Question: {rand_num1}{operator}{rand_num2}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == answer:
            print('Correct!')
            count += 1
        else:
            return print(f'{user_answer} is wrong answer ;(. Correct answer was {answer}\nLet\'s try again, {name}')

    print(f'Congratulations, {name}!')
