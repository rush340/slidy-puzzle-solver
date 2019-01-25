from PIL import Image, ImageColor, ImageDraw
from game import DIRECTIONS, EAST, NORTH, SOUTH, WEST

SPACE_SIZE = 32  # pixels
INDICATOR_ELLIPSE = ((4, 4), (SPACE_SIZE - 5, SPACE_SIZE - 5))
GRID_COLOR = ImageColor.getrgb('#333333')
GRID_WIDTH = 1  # pixels
WALL_COLOR = ImageColor.getrgb('white')
WALL_WIDTH = 2  # pixels


def draw_board(board):
    spaces = board.spaces
    map_width = len(spaces[0])
    map_height = len(spaces)
    map_img_dimensions = (
        map_width * SPACE_SIZE,
        map_height * SPACE_SIZE,
    )
    map_img = Image.new('RGB', map_img_dimensions)

    y_offset = 0
    for row in spaces:
        x_offset = 0
        for space in row:
            space_img = _draw_space(board, space)
            map_img.paste(space_img, (x_offset, y_offset))
            x_offset += SPACE_SIZE
        y_offset += SPACE_SIZE

    # NOTE: this is ugly since it draws over the spaces.
    # I'm doing this for now since I was having issues with a transparent
    # background on the spaces.
    # ideally the spaces would be drawn directly on the map_img, not pasted
    _draw_grid(map_img, spaces)

    map_img.show()


def _draw_grid(map_img, spaces):
    draw = ImageDraw.Draw(map_img)

    num_rows = len(spaces)
    num_columns = len(spaces[0])

    for y_offset in [i * SPACE_SIZE for i in range(1, num_rows)]:
        draw.line(
            ((0, y_offset), (map_img.height, y_offset)),
            fill=GRID_COLOR,
            width=GRID_WIDTH,
        )

    a_row = spaces[0]
    for x_offset in [i * SPACE_SIZE for i in range(1, num_columns)]:
        draw.line(
            ((x_offset, 0), (x_offset, map_img.width)),
            fill=GRID_COLOR,
            width=GRID_WIDTH,
        )


def _draw_space(board, space):
    space_img = Image.new('RGBA', (SPACE_SIZE, SPACE_SIZE))
    draw = ImageDraw.Draw(space_img)

    if space.is_target:
        draw.ellipse(INDICATOR_ELLIPSE, fill=ImageColor.getrgb('red'))

    occupant = board.get_occupant(space)
    if occupant:
        if occupant.is_primary:
            draw.ellipse(INDICATOR_ELLIPSE, fill=ImageColor.getrgb('blue'))
        else:
            draw.ellipse(INDICATOR_ELLIPSE, fill=ImageColor.getrgb('gray'))

    def draw_wall(coords):
        return draw.line(
            coords,
            fill=WALL_COLOR,
            width=WALL_WIDTH,
        )

    wall_bottom = space_img.size[1] - 1 - WALL_WIDTH
    wall_right = space_img.size[0] - 1 - WALL_WIDTH
    wall_direction_coords = {
        NORTH: ((0, 0), (wall_right, 0)),
        EAST: ((wall_right, 0), (wall_right, wall_bottom)),
        SOUTH: ((0, wall_bottom), (wall_right, wall_bottom)),
        WEST: ((0, 0), (0, space_img.size[1] - WALL_WIDTH)),
    }
    for direction in DIRECTIONS:
        if getattr(space.walls, direction):
            draw_wall(wall_direction_coords[direction])

    return space_img


