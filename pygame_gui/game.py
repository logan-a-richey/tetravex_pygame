# game.py

from pygame_gui.click_box import ClickBox
from pygame_gui.tile import Tile

class Game:
    def __init__(self):
        pygame.init()
        self.TILE_SIZE = 100
        self.BOARD_SIZE = 3
        self.SPACING = 50
        self.SCREEN_WIDTH = self.BOARD_SIZE * 2 * self.TILE_SIZE + self.SPACING
        self.SCREEN_HEIGHT = self.BOARD_SIZE * self.TILE_SIZE
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("Tetravex Grids")
        self.font = pygame.font.SysFont(None, 36)
        self.mouse_pos = (0, 0)
        self.mouse_down = False
        self.running = True

        self.grids = {0: [], 1: []}
        for grid in [0, 1]:
            for i in range(self.BOARD_SIZE):
                row = []
                for j in range(self.BOARD_SIZE):
                    cb = ClickBox(self, grid, i, j)
                    row.append(cb)
                self.grids[grid].append(row)

        # Place some tiles randomly on left grid
        import random
        for i in range(self.BOARD_SIZE):
            for j in range(self.BOARD_SIZE):
                tile = Tile(self, random.randint(0, 9), random.randint(0, 9), random.randint(0, 9), random.randint(0, 9))
                self.grids[0][i][j].tile = tile

        self.held_tile = None

    def get_clickbox_at(self, pos):
        for grid_rows in self.grids.values():
            for row in grid_rows:
                for cb in row:
                    if cb.rect.collidepoint(pos):
                        return cb
        return None

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.mouse_down = True
                cb = self.get_clickbox_at(self.mouse_pos)
                if cb and cb.tile:
                    self.held_tile = cb.tile
                    cb.tile = None
            elif event.type == pygame.MOUSEBUTTONUP:
                self.mouse_down = False
                cb = self.get_clickbox_at(self.mouse_pos)
                if cb and not cb.tile and self.held_tile:
                    cb.tile = self.held_tile
                    self.held_tile = None

    def draw(self):
        self.screen.fill("white")
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
