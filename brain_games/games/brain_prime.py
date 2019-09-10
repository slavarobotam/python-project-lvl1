import random
import functools


description = 'Answer "yes" if given number is prime. Otherwise answer "no".\n'


def get_question():  # generating question
    return random.randint(0, 100)


def get_answer(question):  # calculating the correct answer
    num = question
    divisors = [1]
    div = 2  # search starts from 2
    while div <= int(num / div):  # quotient can't be more than num/div
        if num % div == 0:  # found divisor
            divisors.append(div)  # add to list
            num = int(num / div)  # continue search
        else:
            div += 1  # move to next div
    else:
        divisors.append(int(num))  # adding last number as div
    if len(divisors) == 2:
        return 'yes'
    return 'no'
