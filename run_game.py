#!/usr/bin/env python3

import sys
sys.dont_write_bytecode = True

from pygame_gui.game import Game

def main():
    print("[INFO] Running Pygame version!")
    game = Game(3)
    game.run()

if __name__ == "__main__":
    main()

