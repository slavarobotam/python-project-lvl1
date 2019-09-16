#!/usr/bin/env python3

import brain_games.game_engine as engine
from .. import games


def main():
    engine.run(games.brain_even)


if __name__ == '__main__':
    main()
