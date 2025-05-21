# tile.py

import pygame
from random import randint

# lazy colors
#COLORS = {}
#for i in range(10):
#    COLORS[i] = tuple([randint(100,200) for _ in range(3)])
COLORS = {
    0: '#66c5cc',
    1: '#f6cf71',
    2: '#f89c74',
    3: '#dcb0f2',
    4: '#87c55f',
    5: '#5b80d0',
    6: '#fe88b1',
    7: '#8be0a4',
    8: '#b497e7',
    9: '#b3b3b3'
}

class Tile:
    def __init__(self, game, n, e, s, w):
        self.game = game
        self.n = n
        self.e = e
        self.s = s
        self.w = w

        self.x = 0
        self.y = 0

    def update_target(self, tx, ty):
        self.x += (tx - self.x) * 0.1
        self.y += (ty - self.y) * 0.1

    def draw(self):
        TS = self.game.TILE_SIZE
        x = int(self.x)
        y = int(self.y)
        M = (x + TS // 2, y + TS // 2)

        TL = (x, y)
        TR = (x + TS, y)
        BL = (x, y + TS)
        BR = (x + TS, y + TS)

        pygame.draw.polygon(self.game.screen, COLORS[self.n], [M, TL, TR])
        pygame.draw.polygon(self.game.screen, COLORS[self.e], [M, TR, BR])
        pygame.draw.polygon(self.game.screen, COLORS[self.s], [M, BR, BL])
        pygame.draw.polygon(self.game.screen, COLORS[self.w], [M, BL, TL])

        pygame.draw.rect(self.game.screen, (0, 0, 0), (x, y, TS, TS), width=2)

        # Draw numbers
        self.draw_text_center(self.n, x + TS // 2, y + TS * 0.15)
        self.draw_text_center(self.e, x + TS * 0.85, y + TS // 2)
        self.draw_text_center(self.s, x + TS // 2, y + TS * 0.85)
        self.draw_text_center(self.w, x + TS * 0.15, y + TS // 2)

    def draw_text_center(self, value, cx, cy):
        text = self.game.font.render(str(value), True, (0, 0, 0))
        rect = text.get_rect(center=(cx, cy))
        self.game.screen.blit(text, rect)
