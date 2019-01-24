'''
coordinates: 0, 0 is top-left
'''

from collections import namedtuple


SpaceWalls = namedtuple(
    'SpaceWalls',
    ['north', 'east', 'south', 'west'],
    defaults=[False, False, False, False],
)


class GameSpace:
    walls = SpaceWalls()

    def __init__(self, x, y, is_target, walls=None):
        self.coordinates = (x, y)
        self.is_target = is_target

        if walls is not None:
            if not isinstance(walls, SpaceWalls):
                raise Exception('walls must be a SpaceWalls instance')
            self.walls = walls


class SlidyDude:
    def __init__(self, space):
        self.space = space


class MainDude(SlidyDude):
    pass


class Game:
    def __init__(self, board, pieces):
        self.board = board
        self.pieces = pieces

    def get_occupant(self, space):
        for piece in self.pieces:
            if piece.space == space:
                return piece
        return False

    def is_solved(self):
        for piece in self.pieces:
            if isinstance(piece, MainDude) and piece.space.is_target:
                return True
        return False

    def move_piece(self, piece, direction):
        def move_coordinate(coordinates, direction):
            x, y = coordinates
            if direction == 'north':
                return x, y - 1
            elif direction == 'east':
                return x + 1, y
            elif direction == 'south':
                return x, y + 1
            elif direction == 'west':
                return x - 1, y
            else:
                raise Exception('invalid direction')

        def opposite_direction(direction):
            if direction == 'north':
                return 'south'
            elif direction == 'south':
                return 'north'
            elif direction == 'east':
                return 'west'
            elif direction == 'west':
                return 'east'
            else:
                raise Exception('invalid direction')

        def within_board_bounds(self, coordinates):
            x, y = coordinates
            return y >= 0 and y < len(self.board) and x >=0 and x < len(self.board[0])

        def move_single_space(piece, direction):
            # can't move if there is a wall in that direction on the current space
            if getattr(piece.space.walls, direction):
                return False

            dest_coords = move_coordinate(piece.space.coordinates, direction)
            dest_x, dest_y = dest_coords

            # can't move off of board
            if not within_board_bounds(self, dest_coords):
                return False

            dest_space = self.board[dest_y][dest_x]

            # can't move if destination space has a wall keeping us out from this direction
            if getattr(dest_space.walls, opposite_direction(direction)):
                return False

            # can't move if destination space is already occupied
            if self.get_occupant(dest_space):
                return False

            piece.space = dest_space
            return True

        while move_single_space(piece, direction):
            pass

    def copy(self):
        copied_pieces = [
            type(piece)(piece.space)
            for piece in self.pieces
        ]
        return Game(self.board, copied_pieces)
