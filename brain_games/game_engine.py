def new_game(name, game):
    count = 0
    while count < 3:
        question = game.get_question()
        answer = game.get_answer(question)
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
