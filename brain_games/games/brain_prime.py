import random


description = "Answer 'yes' if given number is prime. Otherwise answer 'no'.\n"


def get_question():
    """Generate question."""
    return random.randint(0, 100)


def get_answer(num):
    """
    Checking if the number is prime.

    Returns:
        answer (str): 'yes' if prime and 'not' if not prime
    """
    divisors = []  # list of simple divisors
    div = 2  # search starts from 2
    while div <= int(num / div):  # quotient can't be more than num/div
        if num % div == 0:  # if found divisor
            divisors.append(div)  # add to list
            num = int(num / div)  # continue search
        else:
            div += 1  # move to next div
    else:
        divisors.append(int(num))  # adding last number as div
    if len(divisors) == 1 and divisors != [1]:  # 1 is not prime number
        return 'yes'
    return 'no'
