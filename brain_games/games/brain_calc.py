# !/usr/bin/.venv python

import random


MIN_NUMBER = 0
MAX_NUMBERV = 10
ANSWER_TEXT = 'What is the result of the expression?'


def get_right_answer(first_number, second_number, operation):

    if operation == '+':
        result = first_number + second_number

    elif operation == '-':
        result = first_number - second_number

    else:
        result = first_number * second_number

    return result


def get_question():

    first_number = random.randint(MIN_NUMBER, MAX_NUMBERV)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBERV)
    operation = random.choice(['+', '-', '*'])
    right_answer = get_right_answer(first_number, second_number, operation)
    question = f'{first_number} {operation} {second_number}'
    return (question, right_answer)


def is_valid_answer(answer):
    return answer.lstrip("-").isdigit()


def check_answer(right_answer, answer):
    answer = int(answer)

    if answer != right_answer:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}')

    return answer == right_answer
