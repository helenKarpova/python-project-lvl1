# !/usr/bin/.venv python

import random

MIN_NUMBER = 0
MAX_NUMBER = 100
ANSWER_TEXT = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question():
    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = True if guess_number % 2 == 0 else False

    return (guess_number, right_answer)


def is_valid_answer(answer):
    return answer.lower() in ('yes', 'no')


def check_answer(right_answer, answer):
    user_answer = answer.lower() == 'yes'
    return user_answer == right_answer
