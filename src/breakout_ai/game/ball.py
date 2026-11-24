import math
import random

from breakout_ai import config


class Ball:
    def __init__(self, paddle):
        self._x = 0.0
        self._y = 0.0
        self._speed = config.BALL_MIN_SPEED

        self._velocity_x = 0.0
        self._velocity_y = 0.0
        self._speed_step_count = (config.BRICKS_ROWS * config.BRICKS_COLUMNS) // config.BALL_SPEED_STEP_INTERVAL
        self._speed_step_size = (config.BALL_MAX_SPEED - config.BALL_MIN_SPEED) / self._speed_step_count

        self._launched = False

        self._paddle = paddle

        self.reset()

    def get_coordinates(self):
        return self._x, self._y

    def launch(self):
        if self._launched:
            return

        launch_angle = math.radians(random.uniform(config.BALL_LAUNCH_ANGLE_MIN, config.BALL_LAUNCH_ANGLE_MAX))
        self._velocity_x = self._speed * math.cos(launch_angle)
        self._velocity_y = -self._speed * math.sin(launch_angle)

        self._launched = True

    def reset(self):
        self._velocity_x = 0.0
        self._velocity_y = 0.0
        self._launched = False
        self._follow_paddle()

    def update(self):
        if not self._launched:
            self._follow_paddle()
            return

        self._x += self._velocity_x * config.PHYSICS_DT
        self._y += self._velocity_y * config.PHYSICS_DT

    def _follow_paddle(self):
        paddle_x, paddle_y = self._paddle.get_coordinates()
        self._x = paddle_x + config.PADDLE_WIDTH / 2
        self._y = paddle_y - config.BALL_RADIUS - config.BALL_BOTTOM_OFFSET_PADDLE

    def update_speed(self, destroyed_bricks): # This method will later be called when a brick is destroyed
        speed_level = destroyed_bricks // config.BALL_SPEED_STEP_INTERVAL

        new_speed = config.BALL_MIN_SPEED + speed_level * self._speed_step_size

        if new_speed == self._speed:
            return

        factor = new_speed / self._speed

        self._velocity_x *= factor
        self._velocity_y *= factor

        self._speed = new_speed


