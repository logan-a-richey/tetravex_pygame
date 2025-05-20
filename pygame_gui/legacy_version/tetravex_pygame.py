# tetravex_pygame.py

import pygame
import sys
import random
import time
random.seed(time.time())

from pygame_gui.square import Square
from pygame_gui.tile import Tile

class TetravexPygame:
    def __init__(self, BOARD_SIZE=3):
        pygame.init()

        self.TILE_SIZE = 100
        self.SPACING = 50
        sh = (BOARD_SIZE + 1) * self.TILE_SIZE
        sw = (BOARD_SIZE * 2 + 1) * self.TILE_SIZE

        self.screen = pygame.display.set_mode((sw, sh))
        pygame.display.set_caption("Tetravex")
        self.font = pygame.font.SysFont(None, 36)

        self.running = 0
        self.last_tile = None
        self.init_board(BOARD_SIZE)

    def init_board(self, BOARD_SIZE):
        self.BOARD_SIZE = BOARD_SIZE

        self.left_grids = []
        self.right_grids = []

        # Use board as 2D grid [x][y], total width = 2 * BOARD_SIZE
        self.board = [
            [None for _ in range(self.BOARD_SIZE)] for _ in range(self.BOARD_SIZE * 2)
        ]

        self.clicks = []
        self.is_solved = 0

        for i in range(BOARD_SIZE ** 2):
            mi = i // BOARD_SIZE
            mj = i % BOARD_SIZE

            rgb = (200, 200, 200)

            sq1 = Square(self, 0, mi, mj, rgb)
            sq2 = Square(self, 1, mi, mj, rgb)

            n, e, s, w = [random.randint(0, 9) for _ in range(4)]
            tile = Tile(self, mi, mj, n, e, s, w)

            # Match edges with top/left neighbors for solvability
            if mi > 0:
                tile.n = self.board[mj][mi - 1].s
            if mj > 0:
                tile.w = self.board[mj - 1][mi].e

            tile.i = mi
            tile.j = mj

            self.board[mj][mi] = tile  # store in left grid only

            self.left_grids.append(sq1)
            self.right_grids.append(sq2)

        self.shuffle_tiles()

    def shuffle_tiles(self):
        # Flatten left grid tiles
        left_tiles = [
            self.board[x][y]
            for x in range(self.BOARD_SIZE)
            for y in range(self.BOARD_SIZE)
            if self.board[x][y] is not None
        ]

        # Shuffle them
        random.shuffle(left_tiles)

        # Put them back and update tile positions
        idx = 0
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                tile = left_tiles[idx]
                self.board[x][y] = tile
                tile.j = x
                tile.i = y
                idx += 1

    def get_coord(self, x, y):
        my = y // self.TILE_SIZE

        # LEFT grid
        if 0 <= x < self.BOARD_SIZE * self.TILE_SIZE:
            mx = x // self.TILE_SIZE
            if 0 <= my < self.BOARD_SIZE:
                return (mx, my)

        # RIGHT grid
        offset = self.BOARD_SIZE * self.TILE_SIZE + self.SPACING  # Replace 100 with self.SPACING if defined
        if offset <= x < offset + self.BOARD_SIZE * self.TILE_SIZE:
            mx = (x - offset) // self.TILE_SIZE
            if 0 <= my < self.BOARD_SIZE:
                return (mx + self.BOARD_SIZE, my)

        return None

    def make_move(self, ai, aj, bi, bj):
        tile_a = self.board[ai][aj]
        tile_b = self.board[bi][bj]

        # Swap tiles in the board
        self.board[ai][aj], self.board[bi][bj] = tile_b, tile_a

        # Update tile coordinates
        if tile_a:
            tile_a.j, tile_a.i = bi, bj
        if tile_b:
            tile_b.j, tile_b.i = ai, aj

        res = self.solution_check()
        if res:
            self.is_solved = 1
        else:
            self.is_solved = 0
    
    def solution_check(self):
        return False

    def update(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = 0

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                res = self.get_coord(pos[0], pos[1])
                if res:
                    self.clicks.clear()
                    self.clicks.append(res)
                    # grab tile
                    self.last_tile = self.board[res[0]][res[1]]

            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                res = self.get_coord(pos[0], pos[1])
                if res:
                    self.clicks.append(res)
                    if len(self.clicks) == 2:
                        move = [*self.clicks[0], *self.clicks[1]]
                        print(move)
                        self.make_move(*move)
                
                self.clicks.clear()

                # release tile
                self.last_tile = None


    def draw(self):
        self.screen.fill("white")

        for g in self.left_grids:
            g.draw()
        for g in self.right_grids:
            g.draw()

        # Draw from board
        for x in range(self.BOARD_SIZE * 2):
            for y in range(self.BOARD_SIZE):
                tile = self.board[x][y]
                if tile:
                    if tile == self.last_tile:
                        continue
                    tile.update()
                    tile.draw()
        
        # Grabbed tile drawn on top, following mouse
        if self.last_tile:
            pos = pygame.mouse.get_pos()
            self.last_tile.x = pos[0] - self.TILE_SIZE // 2
            self.last_tile.y = pos[1] - self.TILE_SIZE // 2
            self.last_tile.draw()

        pygame.display.flip()

    def run(self):
        self.running = 1
        while self.running:
            self.update()
            self.draw()

        pygame.quit()
        sys.exit()

