#!/usr/bin/env python3

from pygame_gui.tetravex_pygame import TetravexPygame

def main():
    print("[INFO] Running Pygame version!")
    game = TetravexPygame(3)
    game.run()

if __name__ == "__main__":
    main()

