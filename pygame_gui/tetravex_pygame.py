# tetravex_pygame.py

import pygame
import sys

class Tile:
    def __init__(self):
        self.rect = None

    def update(self):
        pass

    def draw(self):
        pass

class TetravexPygame:
    def __init__(self, board_size=3):
        # game variables
        #self.board_size = board_size
        #self.board = 
        
        pygame.init()
        screen = pygame.display.set_mode((640, 480))
        pygame.display.set_caption("Hello World")
        self.running = 0

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                btn=pygame.mouse
                print ("x = {}, y = {}".format(pos[0], pos[1]))

    def draw(self):
        pass

    def run(self):
        self.running = 1
        while self.running:
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

