from game import Game, GameSpace, MainDude, SlidyDude, SpaceWalls


def generate_7_move_game():
    MAP_WIDTH = 16
    MAP_HEIGHT = 16

    board = [
        [
            GameSpace(x, y, False, SpaceWalls())
            for x, i in enumerate(range(MAP_WIDTH))
        ]
        for y, i in enumerate(range(MAP_HEIGHT))
    ]

    board[5][7].is_target = True

    # center
    board[7][7].walls = SpaceWalls(north=True, west=True)
    board[8][7].walls = SpaceWalls(south=True, west=True)
    board[8][8].walls = SpaceWalls(east=True, south=True)
    board[7][8].walls = SpaceWalls(north=True, east=True)

    # side walls
    board[0][3].walls = SpaceWalls(east=True)
    board[0][10].walls = SpaceWalls(east=True)
    board[4][0].walls = SpaceWalls(south=True)
    board[13][0].walls = SpaceWalls(south=True)
    board[4][15].walls = SpaceWalls(south=True)
    board[8][15].walls = SpaceWalls(south=True)
    board[15][5].walls = SpaceWalls(east=True)
    board[15][11].walls = SpaceWalls(east=True)

    # internal corners
    # bottom left
    board[1][9].walls = SpaceWalls(south=True, west=True)
    board[5][7].walls = SpaceWalls(south=True, west=True)
    board[11][1].walls = SpaceWalls(south=True, west=True)
    board[12][13].walls = SpaceWalls(south=True, west=True)

    # bottom right
    board[2][5].walls = SpaceWalls(east=True, south=True)
    board[4][10].walls = SpaceWalls(east=True, south=True)
    board[11][10].walls = SpaceWalls(east=True, south=True)
    board[12][6].walls = SpaceWalls(east=True, south=True)

    # top right
    board[4][2].walls = SpaceWalls(north=True, east=True)
    board[2][14].walls = SpaceWalls(north=True, east=True)
    board[9][3].walls = SpaceWalls(north=True, east=True)
    board[14][9].walls = SpaceWalls(north=True, east=True)

    # top left
    board[6][1].walls = SpaceWalls(north=True, west=True)
    board[6][12].walls = SpaceWalls(north=True, west=True)
    board[10][8].walls = SpaceWalls(north=True, west=True)
    board[10][13].walls = SpaceWalls(north=True, west=True)
    board[14][2].walls = SpaceWalls(north=True, west=True)

    pieces = [
        MainDude(board[14][7]),
        SlidyDude(board[2][6]),
        SlidyDude(board[5][12]),
        SlidyDude(board[13][6]),
    ]

    return Game(board, pieces)
