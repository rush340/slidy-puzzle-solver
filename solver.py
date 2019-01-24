from game import MainDude, SlidyDude



def hash_game_state(game):
    hash_string = ''
    for piece in game.pieces:
        hash_string += str(piece.space.coordinates)
    return hash_string


def cached_solve(game):
    if game.is_solved():
        return 0, game.copy()

    directions = ('north', 'east', 'south', 'west')
    games = [game]
    moves = 1
    seen_states = set()

    while True:
        next_games = []
        checked = 0
        discarded = 0
        print(f'checking for solutions in {moves} moves')
        for current_game in games:
            game_hash = hash_game_state(current_game)
            seen_states.add(game_hash)
            for piece_index in range(len(current_game.pieces)):
                for direction in directions:
                    checked += 1
                    modified_game = current_game.copy()
                    current_piece = modified_game.pieces[piece_index]
                    origin = current_piece.space
                    modified_game.move_piece(current_piece, direction)
                    if hash_game_state(modified_game) in seen_states:
                        discarded += 1
                        continue
                    if isinstance(current_piece, MainDude):
                        if modified_game.is_solved():
                            print(f'solved in {moves} moves')
                            return moves, modified_game
                    next_games.append(modified_game)
        moves += 1
        print(f'checked: {checked}')
        print(f'discarded: {discarded}')
        games = next_games
