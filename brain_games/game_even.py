from random import randint
import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, ,{name}!')
    return name

def win_string():
    print(f'Congratulations, {name}!')

def loss_string():
    print(f'Let\'s try again, {name}')
    
def even_number():
    welcome_user()
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
            return print(f'"yes" is wrong answer ;(. Correct answer was "no"\n{loss_string}')
        elif even_num and user_answer.lower() == "no":
            return print(f'"no" is wrong answer ;(. Correct answer was "yes"\n{loss_string}')
    win_string()
