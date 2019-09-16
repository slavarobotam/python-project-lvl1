import random


def show_description():
    print("Answer 'yes' if number is even otherwise answer 'no'.")
    print()


def get_question():  # generating question
    return random.randint(0, 100)


def get_answer(question):  # calculating the correct answer
    if question % 2 == 0:
        return 'yes'
    return 'no'
