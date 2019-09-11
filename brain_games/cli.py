import prompt


def welcome():
    """Print greeting for the new user."""
    print("\nWelcome to the Brain Games!")


def get_name():
    """Request name from user."""
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name


def ask(question):
    """Print a question for the user."""
    print('Question: {}'.format(question))


def get_guess():
    """Request guess for the question from user."""
    guess = prompt.string('Your answer: ')
    return guess


def wrong(guess, answer, name):
    """Print message when the user was wrong."""
    print("'{}' is wrong answer ;(. ".format(guess), end='')
    print("Correct answer was '{}'.".format(answer))
    print("Let's try again, {}!".format(name))


def correct():
    """Prints message for user when the answer is correct"""
    print('Correct!')


def congratulations(name):
    """Prints message for user when he won 3 times"""
    print('Congratulations, {}!'.format(name))
