# !/usr/bin/.venv python

import prompt

CNT_ATTEMPTS = 3


def get_answer(guess_number):
    print(f'Question: {guess_number}')
    answer = prompt.string('Your answer: ').lower()

    return answer


def game_flow(module):
    
    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    
    print(module.WELCOME_TEXT)

    attempt = 0

    while attempt < CNT_ATTEMPTS:

        attempt += 1

        result = module.game()

        if result == 2:
            print('Correct!')

        else:
            print(f'''Let's try again, {user_name}!''')
            return

        if attempt == CNT_ATTEMPTS:
            print(f'''Congratulations, {user_name}!''')

