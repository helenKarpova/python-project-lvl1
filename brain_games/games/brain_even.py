# !/usr/bin/.venv python

import random
from brain_games.game_engine import get_answer

MIN_NUMBER = 0
MAX_NUMBER = 100
SUCCESS_EXIT = 2
FAILED_EXIT = 1
WELCOME_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'

def game():

    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    answer = get_answer(guess_number)

    if answer not in ('yes', 'no'):
        return FAILED_EXIT

    answer_ = True if answer == 'yes' else False
    right_answer = True if guess_number % 2 == 0 else False

    if answer_ != right_answer:
        return FAILED_EXIT

    return SUCCESS_EXIT
