#!/usr/bin/env python3
# Visually split grid (offset by row index)

import pygame
import sys

class ClickBox:
    def __init__(self, game, i, j):
        self.game = game
        self.i = i
        self.j = j

        # Determine horizontal offset for "second" grid
        if i >= 3:
            x_offset = game.TILE_SIZE * (game.GRID_COLS + 1)  # add space between logical grids
        else:
            x_offset = 0

        self.rect = pygame.Rect(
            x_offset + j * game.TILE_SIZE,  # x
            (i % 3) * game.TILE_SIZE,       # y (stack rows 0–2 and 3–5 top-down)
            game.TILE_SIZE,
            game.TILE_SIZE
        )

        self.color_fill = (210, 180, 140)  # tan
        self.color_fill_hl = tuple(int(v * 0.80) for v in self.color_fill)
        self.color_fill_cl = tuple(int(v * 0.60) for v in self.color_fill)
        self.color_border = (0, 0, 0)

    def draw(self):
        if self.rect.collidepoint(self.game.mouse_pos):
            color = self.color_fill_cl if self.game.mouse_down else self.color_fill_hl
        else:
            color = self.color_fill

        pygame.draw.rect(self.game.screen, color, self.rect)
        pygame.draw.rect(self.game.screen, self.color_border, self.rect, width=2)


class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 400))
        pygame.display.set_caption("Split Grid Demo")
        self.font = pygame.font.SysFont(None, 36)
        self.mouse_pos = (0, 0)
        self.mouse_down = 0

        self.GRID_ROWS = 6
        self.GRID_COLS = 3
        self.TILE_SIZE = 100

        self.grid = [
            [ClickBox(self, i, j) for j in range(self.GRID_COLS)]
            for i in range(self.GRID_ROWS)
        ]

    def get_square(self):
        for row in self.grid:
            for box in row:
                if box.rect.collidepoint(self.mouse_pos):
                    return (box.i, box.j)
        return None

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = 1
                res = self.get_square()
                if res:
                    print("DOWN", res)

            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = 0
                res = self.get_square()
                if res:
                    print("UP", res)

    def draw(self):
        self.screen.fill("#00aaaa")
        for row in self.grid:
            for box in row:
                box.draw()
        pygame.display.flip()

    def run(self):
        self.running = True
        while self.running:
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()


def main():
    Game().run()

if __name__ == "__main__":
    main()
