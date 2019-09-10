import random
import functools


decription = 'Find the greatest common divisor of given numbers.\n'


def get_question():  # generating question
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = str(num1) + ' ' + str(num2)
    return question


def get_answer(question):  # calculating the correct answer
    num1 = int(question.split()[0])  # parsing num1
    num2 = int(question.split()[1])  # parsing num2

    def get_divisors(number):  # calculating simple divisors
        i = 2  # search starts from 2
        divisors = [1]
        while i <= int(number / i):  # dividend can't be more than n/i for i
            if number % i == 0:  # found divisor
                divisors.append(i)  # add to list
                number = int(number / i)  # continue search
                i = i - 1  # need to check divisor again with new number
            i = i + 1  # checking next i
        divisors.append(int(number))  # adding last number
        return divisors
    div1 = get_divisors(num1)
    div2 = get_divisors(num2)
    common_divisors = [item for item in div1 if item in div2]
    gcd = functools.reduce(lambda x, y: x*y, common_divisors)
    return gcd
