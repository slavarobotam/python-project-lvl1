import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name


welcome = "\nWelcome to the Brain Games!"

asking = 'Question: {}'.format


def get_guess():
    guess = prompt.string('Your answer: ')
    return guess


def wrong_result(guess, answer, name):
    print("Haha loserito! '{}' is wrong answer.".format(guess))
    print("Correct answer was '{}'.".format(answer))
    print("Let's try again, {}!".format(name))


def correct_result():
    print('Correct!')


grats = 'Congratulations, {}!'.format
