import random
import prompt
from brain_games.scripts.game_engine import welcome_user, game_flow


CNT_ATTEMPTS = 3
SUCCESS_EXIT = 2
FAILED_EXIT = 1


def game(user_name, attempt):
    print('What number is missing in the progression?')

    lenght_progression = random.randint(5, 10)
    guess_position = random.randint(0, lenght_progression-1)
    step = random.randint(5, 10)
    next_value = random.randint(5, 10)
    regression_values = []
    position = 1

    while position <= lenght_progression:
        regression_values.append(next_value)
        next_value += step
        position += 1

    right_answer = regression_values[guess_position]
    regression_values[guess_position] = str('..')
    progression = ' '.join(str(e) for e in regression_values)
    print(f'Question: {progression}')
    answer = prompt.integer('Your answer: ')

    if answer != right_answer:
        print(f'{answer} is wrong answer ;(. Correct answer was {right_answer}')
        return FAILED_EXIT

    return SUCCESS_EXIT


def main():
    user_name = welcome_user()
    game_flow(CNT_ATTEMPTS, game, user_name)


if __name__ == '__main__':
    main()
