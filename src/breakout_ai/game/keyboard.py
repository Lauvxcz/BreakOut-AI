import pygame


class Keyboard:
    def __init__(self, paddle, ball):
        self._paddle = paddle
        self._ball = ball

    def input_handler(self):
        keys = pygame.key.get_pressed()

        self._input_paddle(keys)
        self._input_ball(keys)

    def _input_paddle(self, keys):
        left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

        if left and not right:
            self._paddle.direction = -1

        elif right and not left:
            self._paddle.direction = 1

        else:
            self._paddle.direction = 0

    def _input_ball(self, keys):
        start = keys[pygame.K_SPACE]
        if start:
            self._ball.launch()