from game import Board, Space, SpaceWalls


def generate_7_move_board():
    MAP_WIDTH = 16
    MAP_HEIGHT = 16

    spaces = [
        [
            Space(x, y, False, SpaceWalls())
            for x, i in enumerate(range(MAP_WIDTH))
        ]
        for y, i in enumerate(range(MAP_HEIGHT))
    ]

    spaces[5][7].is_target = True

    # center
    spaces[7][7].walls = SpaceWalls(north=True, west=True)
    spaces[8][7].walls = SpaceWalls(south=True, west=True)
    spaces[8][8].walls = SpaceWalls(east=True, south=True)
    spaces[7][8].walls = SpaceWalls(north=True, east=True)

    # side walls
    spaces[0][3].walls = SpaceWalls(east=True)
    spaces[0][10].walls = SpaceWalls(east=True)
    spaces[4][0].walls = SpaceWalls(south=True)
    spaces[13][0].walls = SpaceWalls(south=True)
    spaces[4][15].walls = SpaceWalls(south=True)
    spaces[8][15].walls = SpaceWalls(south=True)
    spaces[15][5].walls = SpaceWalls(east=True)
    spaces[15][11].walls = SpaceWalls(east=True)

    # internal corners
    # bottom left
    spaces[1][9].walls = SpaceWalls(south=True, west=True)
    spaces[5][7].walls = SpaceWalls(south=True, west=True)
    spaces[11][1].walls = SpaceWalls(south=True, west=True)
    spaces[12][13].walls = SpaceWalls(south=True, west=True)

    # bottom right
    spaces[2][5].walls = SpaceWalls(east=True, south=True)
    spaces[4][10].walls = SpaceWalls(east=True, south=True)
    spaces[11][10].walls = SpaceWalls(east=True, south=True)
    spaces[12][6].walls = SpaceWalls(east=True, south=True)

    # top right
    spaces[4][2].walls = SpaceWalls(north=True, east=True)
    spaces[2][14].walls = SpaceWalls(north=True, east=True)
    spaces[9][3].walls = SpaceWalls(north=True, east=True)
    spaces[14][9].walls = SpaceWalls(north=True, east=True)

    # top left
    spaces[6][1].walls = SpaceWalls(north=True, west=True)
    spaces[6][12].walls = SpaceWalls(north=True, west=True)
    spaces[10][8].walls = SpaceWalls(north=True, west=True)
    spaces[10][13].walls = SpaceWalls(north=True, west=True)
    spaces[14][2].walls = SpaceWalls(north=True, west=True)

    primary_piece = (7, 14)
    secondary_pieces = (
        (6, 2),
        (12, 5),
        (6, 13),
    )
    return Board(spaces, primary_piece, secondary_pieces)
