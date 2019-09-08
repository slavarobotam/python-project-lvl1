import prompt


def get_name():
    name = prompt.string('May I have your name? ')
    print("Hello, {}!\n".format(name))
    return name


welcome = "Welcome to the Brain Games!"

game_description = {
    'brain_even.py': 'Answer "yes" if number even otherwise answer "no".',
    'brain_calc.py': 'What is the result of the expression?',
    'brain_gcd.py': 'Find the greatest common divisor of given numbers.'
            }
