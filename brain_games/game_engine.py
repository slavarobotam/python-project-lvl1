import brain_games.cli as cli


def new_game(game):
    """
    This is a game engine for Brain Games.

    Parameteres:
        game (module): module with implementation of the game which user chosed
    """
    cli.welcome()  # print welcome to brain games
    print(game.description)  # print game description imported from game file
    name = cli.get_name()  # request user name
    wins = 0  # counter for wins
    while wins < 3:
        question = game.get_question()  # generate question
        answer = game.get_answer(question)  # generate answer
        cli.ask(question)  # print the question for the user
        guess = cli.get_guess()  # receive guess from the user
        if guess == answer:
            cli.correct()  # inform user that he is right
            wins += 1
        else:
            cli.wrong(guess, answer, name)  # inform user he is wrong
            return
    cli.congratulations(name)  # print congratulations for user
