# !/usr/bin/.venv python

import prompt


CNT_ATTEMPTS = 3


def game_flow(game):

    print('Welcome to the Brain Games!')
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')

    print(game.ANSWER_TEXT)

    attempt = 0
    while attempt < CNT_ATTEMPTS:
        attempt += 1
        (question, right_answer) = game.get_question()
        print(f'Question: {question}')

        answer = prompt.string('Your answer: ').lower()
        if not game.is_valid_answer(answer):
            print(f'''Let's try again, {user_name}!''')
            return

        result = game.check_answer(right_answer, answer)

        if not result:
            print(f'''Let's try again, {user_name}!''')
            return

        print('Correct!')

        if attempt == CNT_ATTEMPTS:
            print(f'''Congratulations, {user_name}!''')

       
