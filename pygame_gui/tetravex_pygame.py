# tetravex_pygame.py

import pygame
import sys
import random
import time
random.seed(time.time())

from typing import List, Dict


class Square:
    def __init__(self, game, grid=0, i=0, j=0, color=(100, 100, 100)):
        self.game = game
        self.grid = grid
        self.i = i
        self.j = j
        self.color = color
        self.border_color = (0, 0, 0)
        
        # rect: x, y, width, height
        self.rect = pygame.Rect(
            (j * 100) + grid * (game.board_size*100 + 100), 
            i * 100, 
            100, 
            100
        )

    def update(self):
        pass

    def draw(self):
        pygame.draw.rect(self.game.screen, self.color, self.rect)
        pygame.draw.rect(self.game.screen, self.border_color, self.rect, width=2)

class TetravexPygame:
    def get_random_color(self):
        rgb = tuple([random.randint(100,200) for _ in range(3)])
        return rgb

    def init_board(self, board_size):
        self.board_size = board_size
        self.left_grids = []
        self.right_grids = []

        for i in range(board_size**2):
            mi = i // self.board_size
            mj = i % self.board_size
            rgb = (200,200,200)

            sq1 = Square(self, 0, mi, mj, rgb)
            sq2 = Square(self, 1, mi, mj, rgb)
            
            self.left_grids.append(sq1)
            self.right_grids.append(sq2)


    def __init__(self, board_size=3):
        # init pygame
        pygame.init()
        sh = (board_size + 1) * 100
        sw = (board_size * 2 + 1) * 100

        self.screen = pygame.display.set_mode( (sw, sh) )
        pygame.display.set_caption("Tetravex")
        
        # init game
        self.running = 0
        self.init_board(board_size)

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos=pygame.mouse.get_pos()
                btn=pygame.mouse
                print ("x = {}, y = {}".format(pos[0], pos[1]))
        # TODO add ESC key to also exit game
        return

    def draw(self):
        self.screen.fill("white")

        for g in self.left_grids:
            g.draw()      
        for g in self.right_grids:
            g.draw()

        pygame.display.flip()

    def run(self):
        self.running = 1
        while self.running:
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

