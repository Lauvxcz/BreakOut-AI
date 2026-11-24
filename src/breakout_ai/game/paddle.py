from breakout_ai import config

class Paddle:
    def __init__(self):
        self._x = config.DISPLAY_WIDTH // 2 - config.PADDLE_WIDTH // 2
        self._y = config.GAME_HEIGHT - config.PADDLE_HEIGHT - config.PADDLE_BOTTOM_OFFSET
        self.direction = 0

    def get_coordinates(self):
        return self._x, self._y

    def move(self):
        if self.direction == -1:
            self._move_left()
        elif self.direction == 1:
            self._move_right()

    def _move_left(self):
        self._x -= config.PADDLE_SPEED * config.PHYSICS_DT
        if self._x < 0:
            self._x = 0

    def _move_right(self):
        self._x += config.PADDLE_SPEED * config.PHYSICS_DT
        if self._x > config.DISPLAY_WIDTH - config.PADDLE_WIDTH:
            self._x = config.DISPLAY_WIDTH - config.PADDLE_WIDTH