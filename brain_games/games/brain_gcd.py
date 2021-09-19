# !/usr/bin/.venv python

import random


MIN_NUMBER = 0
MAX_NUMBER = 100
ANSWER_TEXT = 'Find the greatest common divisor of given numbers.'


def is_valid_answer(answer):
    return answer.isdigit()


def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


def get_question():
    first_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    right_answer = gcd_recursion(first_number, second_number)
    return ((first_number, second_number), right_answer)


def check_answer(right_answer, answer):

    if int(answer) != right_answer:
        print(f'\'{answer}\' is wrong answer ;(. \
                Correct answer was \'{right_answer}\'.')

    return int(answer) == right_answer
