import brain_games.cli as cli


def new_game(game):
    print(cli.welcome)
    print(cli.get_description[game.__name__[18:]])  # pass name without path
    name = cli.get_name()
    count = 0
    while count < 3:
        question = game.get_question()
        answer = game.get_answer(question)
        print(cli.asking(question))
        guess = cli.get_guess()
        if guess == answer:
            cli.correct()
            count += 1
        else:
            cli.wrong(guess, answer, name)
            return
    print(cli.grats(name))
