import prompt


def get_run_brain_game(get_question_and_answer, GAME_OPTIONS):
    name = prompt.string('Welcome to the Brain Games!\nMay I have your name? ')
    print(f'Hello, {name}!\n{GAME_OPTIONS}')
    user_attempt = 1
    number_of_rounds = 3
    while user_attempt <= number_of_rounds:
        question, correct_answer = get_question_and_answer()
        user_answer = prompt.string(f'Question: {question}\nYour answer: ')
        if user_answer == correct_answer:
            print('Correct!')
            user_attempt += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            break
    print(f'Congratulations, {name}!')
