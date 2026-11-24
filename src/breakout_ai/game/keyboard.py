import pygame


class Keyboard:
    def __init__(self, paddle):
        self.paddle = paddle

    def input_handler(self):
        keys = pygame.key.get_pressed()

        self._input_paddle(keys)

    def _input_paddle(self, keys):
        left = keys[pygame.K_a] or keys[pygame.K_LEFT]
        right = keys[pygame.K_d] or keys[pygame.K_RIGHT]

        if left and not right:
            self.paddle.direction = -1

        elif right and not left:
            self.paddle.direction = 1

        else:
            self.paddle.direction = 0