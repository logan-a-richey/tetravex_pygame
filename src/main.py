#!/usr/bin/env python3
# main.py

import sys
# stop __pycache__
sys.dont_write_bytecode = True

from scenes.game_manager import GameManager

def main():
    gm = GameManager()
    gm.run()

if __name__ == "__main__":
    main()

