#!/usr/bin/env python3


def main():
    print('Welcome to the Brain Games!')
    import brain_games.cli
    import brain_games.brain_even
    name = brain_games.cli.run()
    brain_games.brain_even.run(name)


if __name__ == '__main__':
    main()
