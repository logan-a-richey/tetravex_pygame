# tile.py

import pygame

from src.pygame_version.colors import TILE_COLORS, COLOR_BLACK, COLOR_WHITE

class Tile:
    count = 0

    def __init__(self, game, n, e, s, w):
        self.label = str(Tile.count)
        Tile.count += 1
        
        self.game = game
        self.n, self.e, self.s, self.w = n, e, s, w

        self.x = 0
        self.y = 0

    def update_colors(self):
        # Set up directional tile colors
        self.tile_colors = {
            'n': TILE_COLORS[self.n],
            'e': TILE_COLORS[self.e],
            's': TILE_COLORS[self.s],
            'w': TILE_COLORS[self.w],
        }

        # Font color chosen based on contrast
        self.font_colors = {
            dir: self.get_font_color(color) for dir, color in self.tile_colors.items()
        }

    def __repr__(self):
        return "Tile(label: {}, N: {}, E: {}, S: {}, W : {})".format(
            self.label, self.n, self.e, self.s, self.w
        )

    def get_string(self) -> str:
        return "{}{}{}{}".format(self.n, self.e, self.s, self.w)

    def get_font_color(self, hex_color: str) -> str:
        '''
        Returns white or black based on perceptual brightness of the color.
        Input in format: #rrggbb
        '''
        r = int(hex_color[1:3], 16)
        g = int(hex_color[3:5], 16)
        b = int(hex_color[5:7], 16)
        luminance = 0.299 * r + 0.587 * g + 0.114 * b
        return COLOR_WHITE if luminance < 128 else COLOR_BLACK

    def update_target(self, tx, ty, alpha=0.1):
        self.x += (tx - self.x) * alpha
        self.y += (ty - self.y) * alpha

    def draw(self):
        TS = self.game.TILE_SIZE
        screen = self.game.screen
        font = self.game.font

        x, y = int(self.x), int(self.y)
        M = (x + TS // 2, y + TS // 2)
        TL = (x, y)
        TR = (x + TS, y)
        BR = (x + TS, y + TS)
        BL = (x, y + TS)

        # Draw the four triangle sections
        pygame.draw.polygon(screen, self.tile_colors['n'], [M, TR, TL])
        pygame.draw.polygon(screen, self.tile_colors['e'], [M, BR, TR])
        pygame.draw.polygon(screen, self.tile_colors['s'], [M, BL, BR])
        pygame.draw.polygon(screen, self.tile_colors['w'], [M, TL, BL])

        # Draw tile border
        pygame.draw.rect(screen, COLOR_BLACK, (x, y, TS, TS), width=3)

        # Draw edge numbers (centered)
        if self.game.show_answer_label:
            self.draw_text_center(self.label, *M, COLOR_WHITE) 
            return
        
        self.draw_text_center(self.n, x + TS // 2, y + TS * 0.15, self.font_colors['n'])
        self.draw_text_center(self.e, x + TS * 0.85, y + TS // 2, self.font_colors['e'])
        self.draw_text_center(self.s, x + TS // 2, y + TS * 0.85, self.font_colors['s'])
        self.draw_text_center(self.w, x + TS * 0.15, y + TS // 2, self.font_colors['w'])

    def draw_text_center(self, value, cx, cy, color):
        text = self.game.font.render(str(value), True, color)
        rect = text.get_rect(center=(cx, cy))
        self.game.screen.blit(text, rect)

