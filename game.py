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


class Space:
    walls = SpaceWalls()

    def __init__(self, x, y, is_target, walls=None):
        self.coordinates = (x, y)
        self.is_target = is_target

        if walls is not None:
            if not isinstance(walls, SpaceWalls):
                raise Exception('walls must be a SpaceWalls instance')
            self.walls = walls


class Piece:
    def __init__(self, space, is_primary=False):
        self.space = space
        self.is_primary = is_primary


class Board:
    def __init__(self, spaces, primary_piece, secondary_pieces=None):
        if secondary_pieces is None:
            secondary_pieces = tuple()

        self.spaces = spaces
        self.primary_piece = Piece(
            self.get_space(*primary_piece),
            is_primary=True,
        )
        self.secondary_pieces = tuple(
            Piece(self.get_space(*piece))
            for piece in secondary_pieces
        )

    @property
    def pieces(self):
        return (self.primary_piece,) + self.secondary_pieces

    def get_space(self, x, y):
        return self.spaces[y][x]

    def get_occupant(self, space):
        for piece in self.pieces:
            if piece.space == space:
                return piece
        return False

    def is_solved(self):
        return self.primary_piece.space.is_target

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

        def within_spaces_bounds(self, coordinates):
            x, y = coordinates
            return (
                y >= 0 and y < len(self.spaces) and
                x >= 0 and x < len(self.spaces[0])
            )

        def move_single_space(piece, direction):
            # can't move if there is a wall in that direction on the current space
            if getattr(piece.space.walls, direction):
                return False

            dest_coords = move_coordinate(piece.space.coordinates, direction)
            dest_x, dest_y = dest_coords

            # can't move off of spaces
            if not within_spaces_bounds(self, dest_coords):
                return False

            dest_space = self.spaces[dest_y][dest_x]

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
        secondary_pieces_coordinates = [
            piece.space.coordinates
            for piece in self.secondary_pieces
        ]
        return Board(
            self.spaces,
            self.primary_piece.space.coordinates,
            secondary_pieces_coordinates,
        )
