import random


def show_description():
    print("What number is missing in the progression?")
    print()


def get_question():
    """
    Generate progression and hide a random number.

    Returns:
        question (str): one string containing the progression
    """
    num1 = random.randint(0, 10)  # randomize first number of progression
    step = random.randint(1, 10)  # randomize step
    num10 = num1 + step * 10    # randomize last number
    array_int = list((range(num1, num10, step)))  # make array of int items
    array = list(map(str, array_int))  # convert to array of str items
    hide = random.randint(0, 9)  # randomize position of hidden number
    secret = '.'  # this will replace hidden number
    question_list = array[:hide] + [secret] + array[hide + 1:]  # new list
    question = " ".join(map(str, question_list))  # join to one string
    return question


def get_answer(question):
    """
    Calculating the missed element of progression.

    Returns:
        answer (str): secret number which was hidden
    """
    array = question.split(' ')
    pos = array.index('.')
    if pos > 1:  # if there is no hidden number among first two items
        step = int(array[1]) - int(array[0])  # calculating step
    else:  # if hidden number among first two items, we take two last numbers
        step = int(array[-1]) - int(array[-2])
    if pos > 0:  # if hidden number is not the first in the array
        answer = int(array[pos - 1]) + step  # take previous item and add step
    else:  # if hidden number is the first in the array
        answer = int(array[pos + 1]) - step  # take next and deduct step
    return str(answer)
