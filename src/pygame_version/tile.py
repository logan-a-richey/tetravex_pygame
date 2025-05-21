# tile.py

import pygame

COLORS = {
    0: '#e6194b',  # Red
    1: '#f58231',  # Orange
    2: '#ffe119',  # Yellow
    3: '#bfef45',  # Lime
    4: '#3cb44b',  # Green
    5: '#42d4f4',  # Cyan
    6: '#4363d8',  # Blue
    7: '#911eb4',  # Violet
    8: '#f032e6',  # Pink
    9: '#a9a9a9'   # Gray
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
        
    def get_string(self) -> str:
        return "{}{}{}{}".format(self.n, self.e, self.s, self.w)

    def update_target(self, tx, ty):
        self.x += (tx - self.x) * 0.1
        self.y += (ty - self.y) * 0.1

    def draw(self):
        TS = self.game.TILE_SIZE

        # relative pixel position of tile
        x = int(self.x)
        y = int(self.y)

        # pixel center of tile
        M = (x + TS // 2, y + TS // 2)

        # pixel corners of square
        TL = (x, y)
        TR = (x + TS, y)
        BL = (x, y + TS)
        BR = (x + TS, y + TS)

        pygame.draw.polygon(self.game.screen, COLORS[self.n], [M, TL, TR])
        pygame.draw.polygon(self.game.screen, COLORS[self.e], [M, TR, BR])
        pygame.draw.polygon(self.game.screen, COLORS[self.s], [M, BR, BL])
        pygame.draw.polygon(self.game.screen, COLORS[self.w], [M, BL, TL])

        # tile border
        pygame.draw.rect(self.game.screen, (0, 0, 0), (x, y, TS, TS), width=2)

        # draw numbers
        self.draw_text_center(self.n, x + TS // 2, y + TS * 0.15)
        self.draw_text_center(self.e, x + TS * 0.85, y + TS // 2)
        self.draw_text_center(self.s, x + TS // 2, y + TS * 0.85)
        self.draw_text_center(self.w, x + TS * 0.15, y + TS // 2)

    def draw_text_center(self, value, cx, cy):
        text = self.game.font.render(str(value), True, (0, 0, 0))
        rect = text.get_rect(center=(cx, cy))
        self.game.screen.blit(text, rect)

