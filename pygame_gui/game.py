# game.py

import pygame
from pygame_gui.click_box import ClickBox
from pygame_gui.tile import Tile
import random

class Game:
    def __init__(self, board_size=3):
        pygame.init()
        self.TILE_SIZE = 100
        self.BOARD_SIZE = board_size
        self.SPACING = 50 # space between the two grids
        self.SCREEN_WIDTH = self.BOARD_SIZE * 2 * self.TILE_SIZE + self.SPACING * 3
        self.SCREEN_HEIGHT = self.BOARD_SIZE * self.TILE_SIZE + self.SPACING * 2
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Tetravex Grids")
        
        self.font = pygame.font.SysFont(None, 36)
        self.mouse_pos = (0, 0)
        self.mouse_down = False
        
        self.running = True

        self.init_board()

    def init_board(self):
        # init grid
        self.grids = {0: [], 1: []}
        for grid in [0, 1]:
            for i in range(self.BOARD_SIZE):
                row = []
                for j in range(self.BOARD_SIZE):
                    cb = ClickBox(self, grid, i, j)
                    row.append(cb)
                self.grids[grid].append(row)

        # create tiles    
        tiles = []
        for i in range(self.BOARD_SIZE):
            row = []
            for j in range(self.BOARD_SIZE):
                n, e, s, w = [random.randint(0, 9) for _ in range(4)]
                tile = Tile(self, n, e, s, w)

                if i > 0:
                    tile.n = tiles[(i - 1) * self.BOARD_SIZE + j].s
                if j > 0:
                    tile.w = tiles[i * self.BOARD_SIZE + (j - 1)].e

                tiles.append(tile)

        # shuffle tiles
        random.shuffle(tiles)

        # rearrange tiles
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                tile = tiles[i * self.BOARD_SIZE + j]
                tile.i = i
                tile.j = j
                self.grids[0][i][j].tile = tile

        self.held_tile = None

    def get_clickbox_at(self, pos):
        for grid_rows in self.grids.values():
            for row in grid_rows:
                for cb in row:
                    if cb.rect.collidepoint(pos):
                        return cb
        return None
    
    def on_mouse_down(self):
        self.mouse_down = True
        cb = self.get_clickbox_at(self.mouse_pos)
        if cb and cb.tile:
            self.held_tile = cb.tile
            self.held_tile_origin = cb
            cb.tile = None
    
    def on_mouse_up(self):
        self.mouse_down = False
        if not self.held_tile:
            return

        cb = self.get_clickbox_at(self.mouse_pos)

        if cb:
            if cb.tile:
                # Swap
                old_tile = cb.tile
                cb.tile = self.held_tile

                # Try to return old tile to held_tile_origin
                if self.held_tile_origin and not self.held_tile_origin.tile:
                    self.held_tile_origin.tile = old_tile
                else:
                    # No room — hold onto it
                    self.held_tile = old_tile
                    return
            else:
                cb.tile = self.held_tile
        else:
            # Invalid drop — snap back to origin
            if self.held_tile_origin and not self.held_tile_origin.tile:
                self.held_tile_origin.tile = self.held_tile
            else:
                # Optional fallback: discard or hold
                pass

        self.held_tile = None
        self.held_tile_origin = None
        
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.on_mouse_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.on_mouse_up()
    
    def draw(self):
        self.screen.fill("#77aaaa")
        for grid_rows in self.grids.values():
            for row in grid_rows:
                for cb in row:
                    cb.draw()

        if self.held_tile:
            x, y = pygame.mouse.get_pos()
            self.held_tile.update_target(x - self.TILE_SIZE // 2, y - self.TILE_SIZE // 2)
            self.held_tile.draw()

        pygame.display.flip()

    def run(self):
        while self.running:
            self.mouse_pos = pygame.mouse.get_pos()
            self.handle_events()
            self.draw()
        pygame.quit()
