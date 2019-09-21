#!/usr/bin/env python3

import brain_games.game_engine as engine
from brain_games import games


def main():
    engine.run(games.brain_progression)


if __name__ == '__main__':
    main()
