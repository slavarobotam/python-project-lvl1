def run():
    count = 0
    while count < 3:
        if new_game():
            count += 1
        else:
            print('Haha loserito')
            return
    print('Grats winerito')
    

def new_game():
    import random
    question = random.randint(0, 100)
    print('Question:', question)
    answer = input('Your answer: ')
    return answer_check(answer, question)
    

def answer_check(answer, question):
    answers = {'yes': 0,
               'no': 1}
    any_other_answer = -1
    result = answers.setdefault(answer, any_other_answer)
    return question % 2 == result