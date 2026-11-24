import time

import pygame

from breakout_ai import config
from breakout_ai.game.ball import Ball
from breakout_ai.game.bricks import Bricks
from breakout_ai.game.display import Display
from breakout_ai.game.game_stats import GameStats
from breakout_ai.game.keyboard import Keyboard
from breakout_ai.game.paddle import Paddle

class Main:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Breakout AI")

        self.screen = pygame.display.set_mode((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))

        self.hud_surface = pygame.Surface((config.DISPLAY_WIDTH, config.HUD_HEIGHT))
        self.game_surface = pygame.Surface((config.DISPLAY_WIDTH, config.GAME_HEIGHT))

        self.clock = pygame.time.Clock()
        self.running = True

        # Objects
        self.game_stats = GameStats()
        self.bricks = Bricks()
        self.paddle = Paddle()
        self.ball = Ball(self.paddle, self.game_stats)
        self.keyboard = Keyboard(self.paddle, self.ball)
        self.display = Display(self.hud_surface, self.game_surface, self.paddle, self.ball, self.bricks, self.game_stats)

        # Variables
        self._previous_time = time.perf_counter()
        self._accumulator = 0

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # FPS Limit
            self.clock.tick(config.TARGET_FPS)

            # Background
            self.hud_surface.fill(config.HUD_COLOR)
            self.game_surface.fill(config.GAME_COLOR)

            self.keyboard.input_handler()

            self._physics_handler()

            self.display.render()

            # Update Screen
            self.screen.blit(self.hud_surface, (0, 0))
            self.screen.blit(self.game_surface, (0, config.HUD_HEIGHT))
            pygame.display.flip()

        pygame.quit()


    def _physics_handler(self):
        now = time.perf_counter()
        delta_time = now - self._previous_time
        self._previous_time = now

        self._accumulator += delta_time * config.TIME_SCALE

        while self._accumulator > config.PHYSICS_DT:
            self._accumulator -= config.PHYSICS_DT

            self.paddle.move()
            self.ball.update()

if __name__ == "__main__":
    main = Main()
    main.run()