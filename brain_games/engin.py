import prompt

# game_options
game_calc = 'What is the result of the expression?'
game_even = 'Answer "yes" if the number is even, otherwise answer "no".'
game_gcd = 'Find the greatest common divisor of given numbers.'
game_progression = 'What number is missing in the progression?'
game_prime = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_run_games(get_question_and_answer, game_options):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{game_options}')
    user_attempt = 1
    attempts = 3
    while user_attempt <= attempts:
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            user_attempt += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer is '{correct_answer}'.\nLet's try again, {name}!")
            user_attempt = 1
    print(f'Congratulations, {name}!')
