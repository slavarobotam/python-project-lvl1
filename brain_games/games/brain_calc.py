def question_generator():
    import random
    num1 = str(random.randint(0, 100))
    num2 = str(random.randint(0, 100))
    operation = random.choice(['+', '-', '*'])
    question = num1 + ' ' + operation + ' ' + num2
    answer = str(eval(question))
    return question, answer
