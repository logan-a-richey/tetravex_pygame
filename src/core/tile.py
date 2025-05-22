# new tile.py

import pygame
from typing import Tuple

class Tile:
    def __init__(self, 
        manager,
        values: Tuple[int, int, int, int],
        label: int
    ):
        self.manager = manager
        self.n, self.e, self.s, self.w = values
        self.label = label

    def get_string(self) -> str:
        return "{}{}{}{}".format(
            self.n, 
            self.e, 
            self.s, 
            self.w 
        )

    def rerender(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass

