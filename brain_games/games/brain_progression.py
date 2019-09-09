import random


def get_question():  # generating question
    num1 = random.randint(0, 10)
    step = random.randint(1, 10)
    num10 = num1 + step * 10
    array_int = list((range(num1, num10, step)))
    array = list(map(str, array_int))
    hide = random.randint(0, 9)
    secret = '.'
    question_list = array[:hide] + [secret] + array[hide + 1:]
    question = " ".join(map(str, question_list))
    return question


def get_answer(question):  # calculating the correct answer
    array = question.split(' ')
    pos = array.index('.')
    if pos > 1:
        step = int(array[1]) - int(array[0])
    else:
        step = int(array[-1]) - int(array[-2])
    if pos > 0:
        answer = int(array[pos - 1]) + step
    else:
        answer = int(array[pos + 1]) - step
    return str(answer)
