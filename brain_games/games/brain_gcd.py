import random
import functools


def show_description():
    print('Find the greatest common divisor of given numbers.')
    print()


def get_question():
    """
    Generate two numbers and joins them to a string.

    Returns:
        question (str): two numbers one string
        answer (str): greatest common divisor
    """
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = '{} {}'.format(num1, num2)
    answer = get_gcd(num1, num2)
    return question, answer


def get_gcd(num1, num2):
    """Calculate greatest common divisor using Euclid's algorithm."""
    if num1 > num2:
        big = num1
        small = num2
    else:
        big = num2
        small = num1
    while True:
        remainder = big % small
        if remainder == 0:
            gcd = str(small)
            break
        big = small
        small = remainder
    return gcd
