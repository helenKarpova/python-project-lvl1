

from brain_games.scripts.game_engine import welcome_user, game_flow
import random
import prompt

CNT_ATTEMPTS = 3
MIN_NUMBER = 0
MAX_NUMBER = 100
SUCCESS_EXIT = 2
FAILED_EXIT = 1
FAILED_PARAM_EXIT = 0


def is_prime(guess_number):
    d = 2
    while guess_number % d != 0:
        d += 1
    return d == guess_number


def game(user_name, attempt):
    if attempt == 1:
        print('Answer "yes" if given number is prime. Otherwise answer "no".')

    guess_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {guess_number}')
    user_answer = prompt.string('Your answer: ')

    if user_answer.lower() not in ('yes', 'no'):
        return FAILED_PARAM_EXIT

    user_answer = True if user_answer.lower() == 'yes' else False
    right_answer = is_prime(guess_number)

    if user_answer != right_answer:
        return FAILED_EXIT

    return SUCCESS_EXIT


def main():
    user_name = welcome_user()
    game_flow(CNT_ATTEMPTS, game, user_name)


if __name__ == '__main__':
    main()
