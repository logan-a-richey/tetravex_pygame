# puzzle_generator.py

import random

from typing import List
from core.tile import Tile

class PuzzleGenerator:
    ''' creates a Tetravex Puzzle using my <class Tile> asset '''

    @staticmethod
    def generate_puzzle(self, board_size=3) -> List[List[Tile]]:
        '''
        @param  board_size: int
        @return 2-dim array of <class Tile>
        '''

        matrix = [[None for _ in range(board_size)] for _ in range(board_size)]
        tiles = []
        for i in range(board_size ** 2):
            for j in range(board_size):
                nesw = tuple(random.randint(0, 9) for _ in range(4))
                label = (i * board_size) + (j % board_size)
                tile: Tile = Tile(nesw, label)
                matrix[i][j] = tile

                # check up
                if i > 0:
                    adj: Tile = matrix[i-1][j] 
                    tile.n = adj.s
                
                # check left
                if j > 0:
                    adj: Tile = matrix[i][j-1]
                    tile.w = adj.e 

                tile.rerender()
                tiles.append(tile)

        # shuffle the tiles (using shared_ptr - like property) 
        random.shuffle(tiles)

        # rearrange the matrix
        for iter, tile in enumerate(tiles):
            i = iter // board_size
            j = iter % board_size
            matrix[i][j] = tile

        return matrix
