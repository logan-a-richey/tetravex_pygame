import pygame

from src.pygame_version.colors import COLOR_RED

class BadRect:
    def __init__(self, game, cb):
        self.game = game
        self.pos = (cb.rect.x, cb.rect.y)
        self.dim = (cb.rect.w, cb.rect.h)

        self.surface = pygame.Surface(self.dim)
        self.surface.set_alpha(100)
        self.surface.fill(COLOR_RED)

    def draw(self):
        self.game.screen.blit(self.surface, self.pos)
