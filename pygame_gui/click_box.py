# click_box.py

import pygame

class ClickBox:
    def __init__(self, game, grid, i, j):
        self.game = game
        self.grid = grid  # 0 = left grid, 1 = right grid
        self.i = i
        self.j = j

        self.color_fill = (210, 180, 140)
        self.color_border = (0, 0, 0)

        x_offset = grid * (game.BOARD_SIZE * game.TILE_SIZE + game.SPACING)
        self.rect = pygame.Rect(
            j * game.TILE_SIZE + x_offset,
            i * game.TILE_SIZE,
            game.TILE_SIZE,
            game.TILE_SIZE
        )

        self.tile = None  # The tile currently on this square

    def draw(self):
        mouse_over = self.rect.collidepoint(self.game.mouse_pos)
        color = self.color_fill
        if mouse_over:
            color = tuple([v * 0.8 for v in self.color_fill]) if not self.game.mouse_down else tuple([v * 0.6 for v in self.color_fill])
        
        pygame.draw.rect(self.game.screen, color, self.rect)
        pygame.draw.rect(self.game.screen, self.color_border, self.rect, width=2)

        if self.tile:
            self.tile.update_target(self.rect.x, self.rect.y)
            self.tile.draw()
