# game.py

'''
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import warnings
warnings.filterwarnings(
    "ignore",
    message="Your system is avx2 capable.*",
    category=RuntimeWarning
)

import pygame
import random
from typing import List, Dict, Tuple

from src.pygame_version.logger import get_logger
from src.pygame_version.click_box import ClickBox
from src.pygame_version.tile import Tile
from src.pygame_version.colors import COLOR_BACKGROUND, COLOR_RED, COLOR_WHITE
from src.pygame_version.bad_rect import BadRect
'''

class Game:
    def __init__(self, board_size=3):
        # logger setup
        self.logger = get_logger(__name__)
        self.logger.info("Starting Pygame!")

        # pygame setup
        pygame.init()

        # screen setup
        self.TILE_SIZE = 100
        self.BOARD_SIZE = board_size
        self.SPACING = 50 # space between the two grids
        self.SCREEN_WIDTH = self.BOARD_SIZE * 2 * self.TILE_SIZE + self.SPACING * 3
        self.SCREEN_HEIGHT = self.BOARD_SIZE * self.TILE_SIZE + self.SPACING * 2
        
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Tetravex {} x {}".format(self.BOARD_SIZE, self.BOARD_SIZE))
        
        # game setup
        self.font = pygame.font.SysFont(None, 36)
        self.show_answer_label = False

        self.mouse_pos: Tuple[int, int] = (0, 0)
        self.mouse_down: bool = False
        
        self.solved: bool = False
        self.running: bool = True
        
        self.grids: Dict[int, List[List[ClickBox]]] = {0: [], 1: []}
        self.bad_rects: List[BadRect] = []
        self.init_board()

    def init_board(self):
        # init grid
        self.solved = 0
        self.grids: Dict[int, List[List[ClickBox]]] = {0: [], 1: []}
        for grid in range(2):
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

                tile.update_colors()
                tiles.append(tile)

        # shuffle tiles
        random.shuffle(tiles)
        
        # log message
        msg = "New puzzle instantiated: {} {}".format(
            self.BOARD_SIZE,
            " ".join([t.get_string() for t in tiles])
        )
        self.logger.info(msg)

        # rearrange tiles
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                tile = tiles[i * self.BOARD_SIZE + j]
                tile.i = i
                tile.j = j
                self.grids[0][i][j].tile = tile

        self.held_tile = None

    def get_clickbox_at(self, pos):
        for g in range(2):
            for i in range(self.BOARD_SIZE):
                for j in range(self.BOARD_SIZE):
                    cb = self.grids[g][i][j]
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
            # Invalid drop: snap back to origin
            if self.held_tile_origin and not self.held_tile_origin.tile:
                self.held_tile_origin.tile = self.held_tile
            else:
                # TODO - debug
                # Optional fallback: discard or hold
                pass

        self.held_tile = None
        self.held_tile_origin = None

        self.solution_check()

    def solution_check(self):
        is_solved = True
        self.bad_rects.clear()

        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                is_bad_rect = False
                cb = self.grids[1][i][j]
                
                if not cb.tile:
                    is_solved = False
                    continue

                # Check north
                if i > 0:
                    adj = self.grids[1][i-1][j].tile
                    if not adj:
                        is_solved = False
                    if adj and cb.tile.n != adj.s:
                        is_bad_rect = True
                        is_solved = False
                    
                # Check east
                if j < self.BOARD_SIZE - 1:
                    adj = self.grids[1][i][j+1].tile
                    if not adj:
                        is_solved = False
                    if adj and cb.tile.e != adj.w:
                        is_bad_rect = True
                        is_solved = False

                # Check south
                if i < self.BOARD_SIZE - 1:
                    adj = self.grids[1][i+1][j].tile
                    if not adj:
                        is_solved = False
                    if adj and cb.tile.s != adj.n:
                        is_bad_rect = True
                        is_solved = False

                # Check west
                if j > 0:
                    adj = self.grids[1][i][j-1].tile
                    if not adj:
                        is_solved = False
                    if adj and cb.tile.w != adj.e:
                        is_bad_rect = True
                        is_solved = False

                if is_bad_rect:
                    bad_rect = BadRect(self, cb)
                    self.bad_rects.append(bad_rect)
        
        self.solved = is_solved
        if self.solved == True:
            msg = "Puzzle Solved! "
            for i in range(self.BOARD_SIZE):
                for j in range(self.BOARD_SIZE):
                    msg += "{} ".format(self.grids[1][i][j].tile.get_string())
            self.logger.info(msg)

        return is_solved

    def handle_events(self):
        for event in pygame.event.get():
            # exit events
            if event.type == pygame.QUIT:
                self.running = False
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return

            # mouse events
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.on_mouse_down()
            elif event.type == pygame.MOUSEBUTTONUP:
                self.on_mouse_up()
    
    def draw(self):
        # background
        self.screen.fill(COLOR_BACKGROUND)
        
        # draw clickable grid:
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                self.grids[0][i][j].draw()
                self.grids[1][i][j].draw()
        
        # draw clicked tile:
        if self.held_tile:
            x, y = pygame.mouse.get_pos()
            self.held_tile.update_target(x - self.TILE_SIZE // 2, y - self.TILE_SIZE // 2)
            self.held_tile.draw()

        # draw bad hologram
        if self.mouse_down == False:
            for bad_rect in self.bad_rects:
                bad_rect.draw()

        # display solution text:
        if self.solved:
            msg = "Puzzle Solved! "
            text = self.font.render(msg, True, COLOR_WHITE)
            pos = (self.SCREEN_WIDTH // 2, self.SCREEN_HEIGHT - self.SPACING // 2)
            rect = text.get_rect(center=(pos))
            self.screen.blit(text, rect)

        pygame.display.flip()

    def run(self):
        while self.running:
            self.mouse_pos = pygame.mouse.get_pos()
            self.handle_events()
            self.draw()
        
        pygame.quit()
