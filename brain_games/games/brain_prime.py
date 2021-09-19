# !/usr/bin/.venv python

import random

MIN_NUMBER = 0
MAX_NUMBER = 100
ANSWER_TEXT = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(guess_number):
    d = 2
    while guess_number % d != 0:
        d += 1
    return d == guess_number


def get_question():
    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = is_prime(guess_number)
    return (guess_number, right_answer)


def is_valid_answer(answer):
    return answer.lower() in ('yes', 'no')


def check_answer(right_answer, answer):
    user_answer = answer.lower() == 'yes'
    return user_answer == right_answer
