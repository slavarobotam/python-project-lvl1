import random


description = 'Answer "yes" if number even otherwise answer "no".\n'


def get_question():  # generating question
    return random.randint(0, 100)


def get_answer(question):  # calculating the correct answer
    if question % 2 == 0:
        return 'yes'
    return 'no'
