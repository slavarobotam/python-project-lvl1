#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    import brain_games.cli as get_name
    import brain_games.template as template
    import brain_games.games.brain_calc as brain_calc
    template.new_game(get_name.run(), brain_calc.question_generator)


if __name__ == '__main__':
    main()
