import pygame

from breakout_ai import config


class Display:
    def __init__(self, hud_surface, game_surface):
        self.hud_screen = hud_surface
        self.game_screen = game_surface

        self.score_font = pygame.font.Font(config.FONT_PressStart2P_PATH, config.FONT_SCORE_SIZE)

    def render(self):
        # HUD
        self.draw_score()
        self.draw_lives()

        # Game
        self.draw_ball()
        self.draw_paddle()
        self.draw_bricks()

    def draw_score(self):
        score = 100

        score_text = self.score_font.render(f"{score:05d}", True, config.HUD_TEXT_COLOR)
        score_area = pygame.Rect(0, 0, (config.DISPLAY_WIDTH - 200), config.HUD_HEIGHT)
        score_text_rect = score_text.get_rect(center=score_area.center)
        self.hud_screen.blit(score_text, score_text_rect)

    def draw_lives(self):
        lives = 2 # static for the moment

        lives_area = pygame.Rect((config.DISPLAY_WIDTH - 300), 0, 300, config.HUD_HEIGHT)

        total_width = config.MAX_LIVES * config.HEART_WIDTH + (config.MAX_LIVES - 1) * config.HEART_SPACING
        hearts_rect = pygame.Rect(0, 0, total_width, config.HEART_HEIGHT)
        hearts_rect.center = lives_area.center

        for live_index in range(config.MAX_LIVES):
            color = config.HEART_FULL_COLOR if live_index < lives else config.HEART_EMPTY_COLOR

            for row_index, row in enumerate(config.HEART_PATTERN):
                for cell_index, cell in enumerate(row):
                    if cell == "1":
                        pygame.draw.rect(
                            self.hud_screen, color, (cell_index * config.HEART_SCALE + hearts_rect.x + live_index * (
                                        config.HEART_WIDTH + config.HEART_SPACING), row_index * config.HEART_SCALE + hearts_rect.y, config.HEART_SCALE, config.HEART_SCALE)
                        )

    def draw_ball(self):
        ball_x = 400 # static for the moment
        ball_y = 400 # static for the moment
        pygame.draw.circle(self.game_screen, config.BALL_COLOR, (ball_x, ball_y), config.BALL_RADIUS)

    def draw_paddle(self):
        paddle_x = 250 # static for the moment

        pygame.draw.rect(self.game_screen, config.PADDLE_COLOR, (paddle_x, config.PADDLE_Y_COORD, config.PADDLE_WIDTH, config.PADDLE_HEIGHT))

    def draw_bricks(self):
        brick = [[True for _ in range(config.BRICKS_COLUMNS)] for _ in range(config.BRICKS_ROWS)] # static for the moment

        for row in range(config.BRICKS_ROWS):
            for column in range(config.BRICKS_COLUMNS):
                if brick[row][column]:
                    pygame.draw.rect(self.game_screen, config.BRICKS_ROW_COLORS[row], (
                        config.BRICKS_FIRST_COLUMN_X + column * (config.BRICKS_WIDTH + config.BRICKS_SPACING_H), config.BRICKS_FIRST_ROW_Y + row * (
                                config.BRICKS_HEIGHT + config.BRICKS_SPACING_V), config.BRICKS_WIDTH, config.BRICKS_HEIGHT))