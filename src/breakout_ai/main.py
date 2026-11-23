import pygame

from breakout_ai import config
from breakout_ai.game.display import Display

pygame.init()

screen = pygame.display.set_mode((config.DISPLAY_WIDTH, config.DISPLAY_HEIGHT))

hud_surface = pygame.Surface((config.DISPLAY_WIDTH, config.HUD_HEIGHT))
game_surface = pygame.Surface((config.DISPLAY_WIDTH, config.GAME_HEIGHT))

pygame.display.set_caption("Breakout AI")

clock = pygame.time.Clock()
running = True

display = Display(hud_surface, game_surface)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # FPS Limit
    clock.tick(60)

    # Background
    hud_surface.fill(config.HUD_COLOR)
    game_surface.fill(config.GAME_COLOR)

    display.render()

    # Update Screen
    screen.blit(hud_surface, (0, 0))
    screen.blit(game_surface, (0, config.HUD_HEIGHT))
    pygame.display.flip()

pygame.quit()