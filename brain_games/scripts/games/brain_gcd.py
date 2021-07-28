# !/usr/bin/.venv python

from brain_games.scripts.game_engine import welcome_user, game_flow
import random
import prompt

CNT_ATTEMPTS = 3
MIN_NUMBER = 0
MAX_NUMBER = 100
FIRST_ATTEMPT = 0
SUCCESS_EXIT = 2
FAILED_EXIT = 1


def gcd_recursion(num1, num2):
    if num1 == 0:
        return num2
    return gcd_recursion(num2 % num1, num1)


def game(user_name, attempt):
    first_number = random.randint(0, 100)
    second_number = random.randint(0, 100)
    if attempt == FIRST_ATTEMPT:
        print('Find the greatest common divisor of given numbers.')

    print(f'Question: {first_number} {second_number}')
    answer = prompt.integer('Your answer: ')
    right_answer = gcd_recursion(first_number, second_number)

    if answer != right_answer:
        print(f'\'{answer}\' is wrong answer ;(. \
                Correct answer was \'{right_answer}\'.')
        return FAILED_EXIT

    return SUCCESS_EXIT


def main():
    user_name = welcome_user()
    game_flow(CNT_ATTEMPTS, game, user_name)


if __name__ == '__main__':
    main()
