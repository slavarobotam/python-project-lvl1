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
        question, answer = game.get_question()  # generate question
        cli.ask(question)  # print the question for the user
        guess = cli.get_guess()  # receive guess from the user
        if guess != answer:
            cli.inform_about_wrong_answer(guess, answer, name)
            # show message when the answer is wrong
            return
        cli.inform_about_correct_answer()
        # show message when the answer is correct
        wins += 1
    cli.congratulate(name)  # print congratulations for user
