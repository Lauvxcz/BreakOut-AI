from breakout_ai import config


class GameStats:
    def __init__(self):
        self._score = 0
        self._lives = config.INITIAL_LIVES
        self._combo = 0

    def get_score(self):
        return self._score

    def get_lives(self):
        return self._lives

    def get_combo(self):
        return self._combo

    def is_game_over(self):
        return self._lives <= 0

    def reset(self):
        self._score = 0
        self._lives = config.INITIAL_LIVES
        self._combo = 0

    def reset_combo(self):
        self._combo = 0

    def decrement_lives(self):
        self._lives -= 1

    def add_score(self, points):
        self._score += points

    def register_brick_destroyed(self, row):
        self._combo += 1

        base_points = config.BRICKS_POINT_TOP - row * ((config.BRICKS_POINT_TOP - config.BRICKS_POINT_BOTTOM) / (config.BRICKS_ROWS - 1))
        multiplier = 1.0 + (config.BRICKS_POINT_FACTOR_MAX - 1) / config.BRICKS_POINT_FACTOR_STEPS * (self._combo - 1)
        multiplier = min(multiplier, config.BRICKS_POINT_FACTOR_MAX)
        points = round(base_points * multiplier)

        self.add_score(points)

