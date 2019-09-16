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
    """
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = str(num1) + ' ' + str(num2)
    return question


def get_answer(question):
    """
    Calculate the great common divisor.

    Parameteres:
        question (str): string with two numbers
    Returns:
        gcd (str): great common divisor of the numbers
    """
    num1 = int(question.split()[0])  # obtain number 1
    num2 = int(question.split()[1])  # obtain number 2

    def get_divisors(num):
        """Calculating simple divisors for the number."""
        div = 2  # search starts from 2
        divisors = [1]
        while div <= int(num / div):  # quotient can't be more than num/div
            if num % div == 0:  # found divisor
                divisors.append(div)  # add to list
                num = int(num / div)  # continue search
                continue  # need to check this divisor again for new number
            else:
                div += 1  # move to next div
        else:
            divisors.append(int(num))  # adding last number as div
        return divisors
    div1 = get_divisors(num1)  # list of divisors for number 1
    div2 = get_divisors(num2)  # list of divisors for number 1
    common_divisors = []  # list of common divisors
    for item in div1:
        if item in div2:
            div2.remove(item)  # removing duplicates if match
            common_divisors.append(item)
    gcd = functools.reduce(lambda x, y: x*y, common_divisors)
    # muliplexing the items in the list of common divisors
    return str(gcd)
