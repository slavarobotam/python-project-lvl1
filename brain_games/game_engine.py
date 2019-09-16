import brain_games.cli as cli


def run(game):
    """
    This is a game engine for Brain Games.

    Parameteres:
        game (module): module with implementation of the game which user chosed
    """
    cli.welcome()  # print welcome to brain games
    game.show_description()
    # print game description imported from game file
    name = cli.get_name()  # request user name
    wins = 0  # counter for wins
    while wins < 3:
        question = game.get_question()  # generate question
        answer = game.get_answer(question)  # generate answer
        cli.ask(question)  # print the question for the user
        guess = cli.get_guess()  # receive guess from the user
        if guess != answer:
            cli.inform_user_is_wrong(guess, answer, name)
            # show message for user when the answer is wrong
            return
        cli.inform_user_is_right()  # show message when the answer is correct
        wins += 1
    cli.congratulate(name)  # print congratulations for user
