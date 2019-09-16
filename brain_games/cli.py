import prompt


def welcome():
    """Print greeting for the new user."""
    print()
    print("Welcome to the Brain Games!")


def get_name():
    """Request name from user."""
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    print()
    return name


def ask(question):
    """Print a question for the user."""
    print('Question: {}'.format(question))


def get_guess():
    """Request guess for the question from user."""
    guess = prompt.string('Your answer: ')
    return guess


def inform_user_is_wrong(guess, answer, name):
    """Print message when the user was wrong."""
    print("'{}' is wrong answer ;(. Correct answer was '{}'.".format(guess, answer))
    print("Let's try again, {}!".format(name))


def inform_user_is_right():
    """Prints message for user when the answer is correct"""
    print('Correct!')


def congratulate(name):
    """Prints message for user when he won 3 times"""
    print('Congratulations, {}!'.format(name))
