# tile.py

class Tile:
    def __init__(self, game, n, e, s, w):
        self.game = game
        self.n = n
        self.e = e
        self.s = s
        self.w = w

        self.x = 0
        self.y = 0

    def update_target(self, tx, ty):
        self.x += (tx - self.x) * 0.1
        self.y += (ty - self.y) * 0.1

    def draw(self):
        TS = self.game.TILE_SIZE
        x = int(self.x)
        y = int(self.y)
        M = (x + TS // 2, y + TS // 2)

        TL = (x, y)
        TR = (x + TS, y)
        BL = (x, y + TS)
        BR = (x + TS, y + TS)

        pygame.draw.polygon(self.game.screen, (255, 255, 255), [M, TL, TR])
        pygame.draw.polygon(self.game.screen, (200, 200, 200), [M, TR, BR])
        pygame.draw.polygon(self.game.screen, (150, 150, 150), [M, BR, BL])
        pygame.draw.polygon(self.game.screen, (100, 100, 100), [M, BL, TL])

        pygame.draw.rect(self.game.screen, (0, 0, 0), (x, y, TS, TS), width=2)

