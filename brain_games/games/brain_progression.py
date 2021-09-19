# !/usr/bin/.venv python

import random

MIN_NUMBER = 5
MAX_NUMBER = 10
ANSWER_TEXT = 'What number is missing in the progression?'


def get_question():
    lenght_progression = random.randint(MIN_NUMBER, MAX_NUMBER)
    guess_position = random.randint(0, lenght_progression - 1)
    step = random.randint(MIN_NUMBER, MAX_NUMBER)
    next_value = random.randint(MIN_NUMBER, MAX_NUMBER)
    regression_values = []
    position = 1

    while position <= lenght_progression:
        regression_values.append(next_value)
        next_value += step
        position += 1

    right_answer = regression_values[guess_position]
    regression_values[guess_position] = str('..')
    progression = ' '.join(str(e) for e in regression_values)

    return (progression, right_answer)


def is_valid_answer(answer):
    return answer.isdigit()


def check_answer(right_answer, answer):
    return int(answer) == right_answer
