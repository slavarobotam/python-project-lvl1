import random


def get_question():  # generating question
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 100)
    question = str(num1) + ' ' + str(num2)
    return question


def get_answer(question):  # calculating the correct answer
    num1 = int(question.split()[0])  # parsing num1
    num2 = int(question.split()[1])  # parsing num2
    if num1 > num2:  # need to know which num bigger for the method
        big_num, small_num = num1, num2
    else:
        big_num, small_num = num2, num1  # included case when both equal
    if big_num % small_num == 0:  # checking simple case when small_num is gcd
        return str(small_num)
    max_gcd = int(small_num / 2)  # max possible gcd = upper bound of search
    for i in range(max_gcd, 0, -1):  # descending search for common div
        if big_num % i == 0 and small_num % i == 0:
            return str(i)
