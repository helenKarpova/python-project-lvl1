# !/usr/bin/.venv python

import random
import prompt
from brain_games.scripts.game_engine import welcome_user, game_flow


CNT_ATTEMPTS = 3
MIN_NUMBER = 0
MAX_NUMBER = 100
SUCCESS_EXIT = 2
FAILED_EXIT = 1


def game(user_name, attempt):
    if attempt == 1:
        print('Answer "yes" if the number is even, otherwise answer "no".')

    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {guess_number}')
    user_answer = prompt.string('Your answer:')

    if user_answer.lower() not in ('yes', 'no'):
        return 0

    user_answer = True if user_answer.lower() == 'yes' else False
    right_answer = True if guess_number % 2 == 0 else False

    if user_answer != right_answer:
        return FAILED_EXIT

    return SUCCESS_EXIT


def main():
    user_name = welcome_user()
    game_flow(CNT_ATTEMPTS, game, user_name)


if __name__ == '__main__':
    main()
