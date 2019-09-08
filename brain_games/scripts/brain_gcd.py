#!/usr/bin/env python3

import os
import brain_games.cli as cli
import brain_games.game_engine as engine
import brain_games.games.brain_gcd as game


def main():
    print(cli.welcome)
    print(cli.game_description[os.path.basename(__file__)], '\n')
    engine.new_game(cli.get_name(), game)


if __name__ == '__main__':
    main()
