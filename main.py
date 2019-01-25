#!/usr/bin/env python

from maps import generate_7_move_board
from solver import cached_solve
from render import draw_board


def main():
    # generate a board, display it, solve it, and display the solved board
    board = generate_7_move_board()
    draw_board(board)
    moves, solved_board = cached_solve(board)
    draw_board(solved_board)


if __name__ == '__main__':
    main()
