from game import DIRECTIONS


def hash_board_state(board):
    hash_string = ''
    for piece in board.pieces:
        hash_string += str(piece.space.coordinates)
    return hash_string


def cached_solve(board):
    if board.is_solved():
        return 0, board.copy()

    boards = [board]
    moves = 1
    seen_states = set()

    while True:
        next_boards = []
        checked = 0
        discarded = 0
        print(f'checking for solutions in {moves} moves')
        for current_board in boards:
            board_hash = hash_board_state(current_board)
            seen_states.add(board_hash)
            for piece_index in range(len(current_board.pieces)):
                for direction in DIRECTIONS:
                    checked += 1
                    modified_board = current_board.copy()
                    current_piece = modified_board.pieces[piece_index]
                    modified_board.move_piece(current_piece, direction)
                    if hash_board_state(modified_board) in seen_states:
                        discarded += 1
                        continue
                    if current_piece.is_primary:
                        if modified_board.is_solved():
                            print(f'solved in {moves} moves')
                            return moves, modified_board
                    next_boards.append(modified_board)
        moves += 1
        print(f'checked: {checked}')
        print(f'discarded: {discarded}')
        boards = next_boards
