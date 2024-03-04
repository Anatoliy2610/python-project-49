import prompt
def welcome_user(name):
    name = prompt.string('May I have you name? ')    
    if len(name) <= 0:
        name = input()

    else:
        print('Hello, ' + name + '!')
