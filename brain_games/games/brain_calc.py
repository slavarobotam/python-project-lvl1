import random


def show_description():
    print('What is the result of the expression?')
    print()


def get_question():  # generating question
    num1 = str(random.randint(0, 100))
    num2 = str(random.randint(0, 100))
    oper_list = ['+', '-', '*']
    operation = random.choice(oper_list)
    question = num1 + ' ' + operation + ' ' + num2
    return question


def get_answer(question):  # calculating the correct answer
    return str(eval(question))
