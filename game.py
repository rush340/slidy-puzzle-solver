'''
coordinates: 0, 0 is top-left
'''

from collections import namedtuple


NORTH = 'north'
EAST = 'east'
SOUTH = 'south'
WEST = 'west'

DIRECTIONS = {NORTH, SOUTH, EAST, WEST}
OPPOSITE_DIRECTIONS = {
    NORTH: SOUTH,
    SOUTH: NORTH,
    EAST: WEST,
    WEST: EAST,
}


class InvalidDirection(Exception):
    pass


SpaceWalls = namedtuple(
    'SpaceWalls',
    [NORTH, EAST, SOUTH, WEST],
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
        if direction not in DIRECTIONS:
            raise InvalidDirection()

        def move_coordinate(coordinates, direction):
            movers = {
                NORTH: lambda x, y: (x, y - 1),
                EAST: lambda x, y: (x + 1, y),
                SOUTH: lambda x, y: (x, y + 1),
                WEST: lambda x, y: (x - 1, y),
            }
            return movers[direction](*coordinates)

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
            if getattr(dest_space.walls, OPPOSITE_DIRECTIONS[direction]):
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
