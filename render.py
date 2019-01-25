from PIL import Image, ImageColor, ImageDraw


SPACE_DIMENSIONS = (32, 32)
INDICATOR_ELLIPSE = ((4, 4), (SPACE_DIMENSIONS[0] - 5, SPACE_DIMENSIONS[1] - 5))
WALL_COLOR = ImageColor.getrgb('white')
WALL_WIDTH = 2

def draw_game(game):
    spaces = game.spaces
    map_width = len(spaces[0])
    map_height = len(spaces)
    map_img_dimensions = (
        map_width * SPACE_DIMENSIONS[0],
        map_height * SPACE_DIMENSIONS[1],
    )
    map_img = Image.new('RGB', map_img_dimensions)

    def draw_space(space):
        space_img = Image.new('RGB', SPACE_DIMENSIONS)
        draw = ImageDraw.Draw(space_img)

        if space.is_target:
            draw.ellipse(INDICATOR_ELLIPSE, fill=ImageColor.getrgb('red'))

        occupant = game.get_occupant(space)
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
        if space.walls.north:
            draw_wall((
                (0, 0),
                (wall_right, 0),
            ))
        if space.walls.east:
            draw_wall((
                (wall_right, 0),
                (wall_right, wall_bottom),
            ))
        if space.walls.south:
            draw_wall((
                (0, wall_bottom),
                (wall_right, wall_bottom),
            ))
        if space.walls.west:
            draw_wall((
                (0, 0),
                (0, space_img.size[1] - WALL_WIDTH),
            ))

        return space_img

    y_offset = 0
    for row in spaces:
        x_offset = 0
        for space in row:
            space_img = draw_space(space)
            map_img.paste(space_img, (x_offset, y_offset))
            x_offset += SPACE_DIMENSIONS[0]
        y_offset += SPACE_DIMENSIONS[1]

    map_img.show()
