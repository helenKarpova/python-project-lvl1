# !/usr/bin/.venv python

import random
import prompt


CNT_ATTEMPTS = 3
MIN_NUMBER = 0
MAX_NUMBER = 100


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def game(user_name):

    print('Answer "yes" if the number is even, otherwise answer "no".')
    attempt = 0

    while attempt < CNT_ATTEMPTS:
        guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)

        print(f'Question: {guess_number}')
        user_answer = prompt.string('Your answer:')

        if user_answer.lower() not in ('yes', 'no'):
            break

        user_answer = True if user_answer.lower() == 'yes' else False
        right_answer = True if guess_number % 2 == 0 else False

        if user_answer != right_answer:
            print(f'''Let's try again, {user_name}!''')
            break

        print('Correct!')
        attempt += 1

    if attempt == CNT_ATTEMPTS:
        print(f'''Congratulations, {user_name}!''')


def main():
    name = welcome_user()
    game(name)


if __name__ == '__main__':
    main()
