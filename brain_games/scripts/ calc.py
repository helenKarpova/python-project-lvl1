import random
import prompt
from brain_games.game_engine import welcome_user, game_flow
MIN_NUMBER = 0
MAX_NUMBERV = 10
CNT_ATTEMPTS = 3
SUCCESS_EXIT = 2
FAILED_EXIT = 1


def get_answer(first_number, second_number, operation):

    if operation == '+':
        result = first_number + second_number

    elif operation == '-':
        result = first_number - second_number

    else:
        result = first_number * second_number

    return result


def get_example():

    first_number = random.randint(MIN_NUMBER, MAX_NUMBERV)
    second_number = random.randint(MIN_NUMBER, MAX_NUMBERV)
    operation = random.choice(['+', '-', '*'])

    print(f'Question: {first_number} {operation} {second_number}')

    return (first_number, second_number, operation)


def game(user_name, attempt):

    example = get_example()
    answer = prompt.integer('Your answer: ')
    right_answer = get_answer(example[0], example[1], example[2])

    if answer != right_answer:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}')
        return FAILED_EXIT

    return SUCCESS_EXIT
