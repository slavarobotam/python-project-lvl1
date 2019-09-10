import random


description = 'What is the result of the expression?\n'


def get_question():  # generating question
    num1 = str(random.randint(0, 100))
    num2 = str(random.randint(0, 100))
    operation = random.choice(['+', '-', '*'])
    question = num1 + ' ' + operation + ' ' + num2
    return question


def get_answer(question):  # calculating the correct answer
    return str(eval(question))
