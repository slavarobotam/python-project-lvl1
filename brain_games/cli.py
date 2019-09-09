import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name


welcome = "\nWelcome to the Brain Games!"

get_description = {
    'brain_even.py': 'Answer "yes" if number even otherwise answer "no".\n',
    'brain_calc.py': 'What is the result of the expression?\n',
    'brain_gcd': 'Find the greatest common divisor of given numbers.\n'
            }

asking = 'Question: {}'.format


def get_guess():
    guess = prompt.string('Your answer: ')
    return guess


def wrong(guess, answer, name):
    print("Haha loserito! '{}' is wrong answer.".format(guess))
    print("Correct answer was '{}'.".format(answer))
    print("Let's try again, {}!".format(name))


def correct():
    print('Correct!')


grats = 'Congratulations, {}!'.format
