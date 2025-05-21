#!/usr/bin/env python3

import re
import sys
# prevent __pycache__
sys.dont_write_bytecode = True

from src.pygame_version.game import Game

def main():
    size = 3
    if len(sys.argv) >= 2:
        num_match = re.match(r'\d+', sys.argv[1])
        if not num_match:
            print("Usage: ./main.py <board_size_int>")
            exit(1)
        size = int(num_match.group(0))
        if (size < 2 or size > 8):
            print("Usage: size must be between 2 and 8")
            exit(1)

    game = Game(size)
    game.run()

if __name__ == "__main__":
    main()

