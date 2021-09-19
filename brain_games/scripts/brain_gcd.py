# !/usr/bin/.venv python

from brain_games.game_engine import game_flow
from brain_games.games import brain_gcd


def main():
    game_flow(brain_gcd)


if __name__ == '__main__':
    main()
