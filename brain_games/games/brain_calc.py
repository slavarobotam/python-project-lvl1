import random
import operator as oper


def show_description():
    print('What is the result of the expression?')
    print()


def get_question():  # generating question without a single if
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    questions = ['{} {} {}'.format(num1, sign, num2) for sign in '+-*']
    operations = [oper.add, oper.sub, oper.mul]
    question_and_operation = random.choice(list(zip(questions, operations)))
    question = question_and_operation[0]
    answer = str(question_and_operation[1](num1, num2))
    return question, answer
