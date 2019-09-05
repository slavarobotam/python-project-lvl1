#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    import brain_games.cli
    brain_games.cli.run()
    import brain_games.brain_even
    brain_games.brain_even.run()


if __name__ == '__main__':
    main()
