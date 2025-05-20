# square.py

import pygame

class Square:
    ''' single rect for tetravex grid '''
    def __init__(self, game, grid=0, i=0, j=0, color=(100, 100, 100)):
        self.game = game
        self.grid = grid
        self.i = i
        self.j = j
        self.color = color
        self.border_color = (0, 0, 0)
        
        # rect: x, y, width, height
        self.rect = pygame.Rect(
            (j * game.TILE_SIZE) + grid * (game.BOARD_SIZE * game.TILE_SIZE + game.SPACING), 
            i * game.TILE_SIZE, 
            game.TILE_SIZE, 
            game.TILE_SIZE
        )

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        pygame.draw.rect(self.game.screen, self.border_color, self.rect, width=2)

