import prompt


def welcome_user():

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    # print('What is the result of the expresssion?')
    return name


def game_flow(cnt_attempts, func, user_name):
    attempt = 0

    while attempt < cnt_attempts:
        attempt += 1

        result = func(user_name, attempt)

        if result == 2:
            print('Correct!')

        else:
            print(f'''Let's try again, {user_name}!''')
            return

        if attempt == cnt_attempts:
            print(f'''Congratulations, {user_name}!''')
