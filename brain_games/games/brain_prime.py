import random
import math


def show_description():
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    print()


def get_question():
    """
    Generate number and check if it is prime.
    Returns:
        question (str): number from 1 to 100
        answer (str): 'yes' if the number is prime, 'no' otherwise.
    """
    num = random.randint(1, 100)
    if num in {2, 3}:  # check simple cases to skip first numbers
        answer = 'yes'
    elif num == 1 or (num % 2 == 0) or (num % 3 == 0):  # check simple cases
        answer = 'no'
    else:
        max_divisor = int(math.sqrt(num))
        for i in range(5, max_divisor, 2):
            if num % i == 0:
                answer = 'no'
                break
        else:
            answer = 'yes'
    question = str(num)
    return question, answer
