def new_game(name, question_generator):
    count = 0
    while count < 3:
        question, answer = question_generator()
        print('Question:', question)
        guess = input('Your answer: ')
        if guess == answer:
            print('Correct!')
            count += 1
        else:
            print("Haha loserito! '{}' is wrong answer.".format(guess))
            print("Correct answer was '{}'.".format(answer))
            print("Let's try again, {}!".format(name))
            return
    print('Congratulations, {}!'.format(name))
