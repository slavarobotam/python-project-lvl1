import random


def show_description():
    print("What number is missing in the progression?")
    print()


def get_question():
    """
    Generate a progression with a hidden number.

    Returns:
        question (str): one string containing the progression
        answer (str): secret number which was hidden
    """
    num1 = random.randint(0, 10)  # randomize first number of progression
    step = random.randint(1, 10)  # randomize step
    num10 = num1 + step * 10    # calculate last number of progression
    progression = list(map(str, range(num1, num10, step)))  # make sequence
    hidden_pos = random.randint(0, 9)  # randomize position of hidden number
    answer = progression[hidden_pos]  # save answer for return
    progression[hidden_pos] = '.'  # replace the number with '.'
    question = " ".join(progression)  # join to one string
    return question, answer
