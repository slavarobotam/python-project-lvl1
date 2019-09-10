import random


description = 'What number is missing in the progression?\n'


def get_question():  # generating question
    num1 = random.randint(0, 10)
    step = random.randint(1, 10)
    num10 = num1 + step * 10
    array_int = list((range(num1, num10, step)))  # array of int items
    array = list(map(str, array_int))  # array of str items
    hide = random.randint(0, 9)  # position of hidden number
    secret = '.'
    question_list = array[:hide] + [secret] + array[hide + 1:]
    question = " ".join(map(str, question_list))  # join to string
    return question


def get_answer(question):  # calculating the correct answer
    array = question.split(' ')
    pos = array.index('.')
    if pos > 1:  # if there is no hidden number among first two items
        step = int(array[1]) - int(array[0])  # calculating step
    else:  # if hidden number among first two items, we take two last numbers
        step = int(array[-1]) - int(array[-2])
    if pos > 0:  # if hidden number is not the first in the array
        answer = int(array[pos - 1]) + step
    else:  # if hidden number is the first in the array
        answer = int(array[pos + 1]) - step
    return str(answer)
