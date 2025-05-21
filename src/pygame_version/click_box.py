# click_box.py

import pygame

class ClickBox:
    def __init__(self, game, grid, i, j):
        self.game = game
        self.grid = grid  # 0 = left grid, 1 = right grid
        self.i = i
        self.j = j

        self.color_fill = (210, 180, 140)
        self.color_fill_hl = tuple([v * 0.8 for v in self.color_fill])
        self.color_fill_cl = tuple([v * 0.6 for v in self.color_fill])

        self.color_border = (0, 0, 0)
        
        self.bad = 0
        self.color_bad = (255,0,0,200)

        margin_offset = self.game.SPACING
        x_offset = grid * (game.BOARD_SIZE * game.TILE_SIZE + game.SPACING)
        self.rect = pygame.Rect(
            j * game.TILE_SIZE + x_offset + margin_offset,
            i * game.TILE_SIZE + margin_offset,
            game.TILE_SIZE,
            game.TILE_SIZE
        )
        
        # the tile currently on this square
        self.tile = None  

    def draw(self):
        mouse_over = self.rect.collidepoint(self.game.mouse_pos)
        
        # clickbox fill
        color = self.color_fill
        if mouse_over:
            if self.game.mouse_down:
                color = self.color_fill_cl
            else:
                color = self.color_fill_hl
        
        pygame.draw.rect(self.game.screen, color, self.rect)
        
        # clickbox border
        pygame.draw.rect(self.game.screen, self.color_border, self.rect, width=2)

        if self.tile:
            self.tile.update_target(self.rect.x, self.rect.y)
            self.tile.draw()

