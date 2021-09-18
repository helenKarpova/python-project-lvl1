# !/usr/bin/.venv python

from brain_games.game_engine import game_flow
from brain_games.games import brain_even


def main():
    game_flow(brain_even)


if __name__ == '__main__':
    main()