# gameplay_scene.py

import pygame
from scenes.base_scene import BaseScene
# from assets.board import Board
# from assets.tile import Tile
# from assets.bad_rect import BadRect

class GameplayScene(BaseScene):
    ''' contains logic for GamePlay scene logic, updating, and rendering '''
    
    def __init__(self, manager, board_size=3):
        self.manager = manager


        # objects in scene
        self.BOARD_SIZE: int = board_size
        self.TILE_SIZE: int = 100
        self.SPACING: int = 50 # margin spacing between elements

        screen_dim = (
            self.BOARD_SIZE * 2 * self.TILE_SIZE + self.SPACING * 3,
            self.BOARD_SIZE * self.TILE_SIZE + self.SPACING * 2
        )

        # TODO dynamically allow the user to shrink and expand the window
        # resize window for this puzzle
        self.manager.screen = pygame.display.set_mode(screen_dim)
        pygame.display.set_caption("Tetravex {}x{}".format(self.BOARD_SIZE, self.BOARD_SIZE)) 

        pass

    def update(self):
        pass

    def draw(self):
        self.manager.screen.fill("#404040")
