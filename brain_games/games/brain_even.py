import random


def show_description():
    print("Answer 'yes' if number is even otherwise answer 'no'.")
    print()


def get_question():  # generating question
    num = random.randint(0, 100)
    question = str(num)
    if num % 2 == 0:
        answer = 'yes'
    else:
        answer = 'no'
    return question, answer
