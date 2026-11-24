from breakout_ai import config


class Bricks:
    def __init__(self):
        self._bricks = [[True for _ in range(config.BRICKS_COLUMNS)] for _ in range(config.BRICKS_ROWS)]
        self._destroyed_count = 0

        self._brick_bounds = [[] for _ in range(config.BRICKS_ROWS)]
        for row in range(config.BRICKS_ROWS):
            for column in range(config.BRICKS_COLUMNS):
                start_x = config.BRICKS_SIDE_MARGIN + column * (config.BRICKS_WIDTH + config.BRICKS_SPACING_H)
                start_y = config.BRICKS_FIRST_ROW_Y + row * (config.BRICKS_HEIGHT + config.BRICKS_SPACING_V)
                end_x = start_x + config.BRICKS_WIDTH
                end_y = start_y + config.BRICKS_HEIGHT
                self._brick_bounds[row].append((start_x, start_y, end_x, end_y))

    def get_bricks(self):
        return self._bricks

    def get_destroyed_count(self):
        return self._destroyed_count

    def get_brick_bounds(self):
        return self._brick_bounds

    def destroy_brick(self, row, col):
        if row < 0 or row >= config.BRICKS_ROWS or col < 0 or col >= config.BRICKS_COLUMNS:
            return False

        if self._bricks[row][col]:
            self._bricks[row][col] = False
            self._destroyed_count += 1

            return True

        return False

    def is_all_destroyed(self):
        return self._destroyed_count == config.BRICKS_ROWS * config.BRICKS_COLUMNS

    def reset(self):
        self._bricks = [[True for _ in range(config.BRICKS_COLUMNS)] for _ in range(config.BRICKS_ROWS)]
        self._destroyed_count = 0