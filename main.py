#!/usr/bin/env python

from maps import generate_7_move_game
from solver import cached_solve
from render import draw_game


def main():
    game = generate_7_move_game()
    draw_game(game)
    moves, solved_game = cached_solve(game)
    draw_game(solved_game)


if __name__ == '__main__':
    main()
