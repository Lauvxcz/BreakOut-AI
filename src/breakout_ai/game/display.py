import pygame

from breakout_ai import config


class Display:
    def __init__(self, hud_surface, game_surface, paddle, ball, bricks, game_stats):
        self._hud_screen = hud_surface
        self._game_screen = game_surface

        self._score_font = pygame.font.Font(config.FONT_PRESSSTART2P_PATH, config.FONT_SCORE_SIZE)

        self._game_stats = game_stats
        self._paddle = paddle
        self._ball = ball
        self._bricks = bricks


    def render(self):
        # HUD
        self.draw_score()
        self.draw_lives()

        # Game
        self.draw_ball()
        self.draw_paddle()
        self.draw_bricks()

    def draw_score(self):
        score = self._game_stats.get_score()

        score_text = self._score_font.render(f"{score:05d}", True, config.HUD_TEXT_COLOR)
        score_area = pygame.Rect(0, 0, (config.DISPLAY_WIDTH - 200), config.HUD_HEIGHT)
        score_text_rect = score_text.get_rect(center=score_area.center)
        self._hud_screen.blit(score_text, score_text_rect)

    def draw_lives(self):
        lives = self._game_stats.get_lives()

        lives_area = pygame.Rect((config.DISPLAY_WIDTH - 300), 0, 300, config.HUD_HEIGHT)

        total_width = config.INITIAL_LIVES * config.HEART_WIDTH + (config.INITIAL_LIVES - 1) * config.HEART_SPACING
        hearts_rect = pygame.Rect(0, 0, total_width, config.HEART_HEIGHT)
        hearts_rect.center = lives_area.center

        for live_index in range(config.INITIAL_LIVES):
            color = config.HEART_FULL_COLOR if live_index < lives else config.HEART_EMPTY_COLOR

            for row_index, row in enumerate(config.HEART_PATTERN):
                for cell_index, cell in enumerate(row):
                    if cell == "1":
                        pygame.draw.rect(
                            self._hud_screen, color, (cell_index * config.HEART_SCALE + hearts_rect.x + live_index * (
                                        config.HEART_WIDTH + config.HEART_SPACING), row_index * config.HEART_SCALE + hearts_rect.y, config.HEART_SCALE, config.HEART_SCALE)
                        )

    def draw_ball(self):
        x, y = self._ball.get_coordinates()
        pygame.draw.circle(self._game_screen, config.BALL_COLOR, (x, y), config.BALL_RADIUS)

    def draw_paddle(self):
        x, y = self._paddle.get_coordinates()
        pygame.draw.rect(self._game_screen, config.PADDLE_COLOR, (x, y, config.PADDLE_WIDTH, config.PADDLE_HEIGHT))

    def draw_bricks(self):
        bricks = self._bricks.get_bricks()
        brick_bounds = self._bricks.get_brick_bounds()

        for row in range(config.BRICKS_ROWS):
            for column in range(config.BRICKS_COLUMNS):
                if bricks[row][column]:
                    start_x, start_y, end_x, end_y = brick_bounds[row][column]
                    pygame.draw.rect(self._game_screen, config.BRICKS_ROW_COLORS[row], (start_x, start_y, end_x - start_x, end_y - start_y))