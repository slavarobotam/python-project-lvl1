import random
import functools


description = 'Find the greatest common divisor of given numbers.\n'


def get_question():  # generating question
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = str(num1) + ' ' + str(num2)
    return question


def get_answer(question):  # calculating the correct answer
    num1 = int(question.split()[0])  # parsing num1
    num2 = int(question.split()[1])  # parsing num2

    def get_divisors(num):  # calculating simple divisors of number
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
    div1 = get_divisors(num1)
    div2 = get_divisors(num2)
    print(div1, div2)
    common_divisors = []
    for item in div1:
        if item in div2:
            div2.remove(item)  # removing duplicates if match
            common_divisors.append(item)
    gcd = functools.reduce(lambda x, y: x*y, common_divisors)
    return gcd
