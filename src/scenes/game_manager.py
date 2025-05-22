# game_manager.py

import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

import warnings
warnings.filterwarnings(
    "ignore",
    message="Your system is avx2 capable.*",
    category=RuntimeWarning
)

import pygame
from core.logger import get_logger

from typing import Tuple, List, Dict

from scenes.base_scene import BaseScene
from scenes.title_scene import TitleScene
#from scenes.level_select_scene import LevelSelectScene
from scenes.gameplay_scene import GameplayScene
#from scenes.option_scene import OptionScene
#from scenes.highscore_scene import HighscoreScene

class GameManager:
    def __init__(self):
        # logging setup
        self.logger = get_logger(__name__)
        self.logger.info("Starting Pygame!")
        
        # pygame setup
        pygame.init()
        screen_dim: Tuple[int, int] = (400, 400) # default will change later
        self.screen = pygame.display.set_mode(screen_dim)
        pygame.display.set_caption("Tetravex")

        self.running: bool = False
        
        self.current_scene: BaseScene = TitleScene(self)
        
        self.mouse_pos: Tuple[int, int] = (0,0)
        self.is_mouse_down: bool = False
    
    def on_mouse_down(self):
        pass

    def on_mouse_up(self):
        pass

    def poll_events(self):
        self.mouse_pos = pygame.mouse.get_pos()

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

    def update_scene(self):
        self.current_scene.update()
    
    def draw_scene(self):
        self.current_scene.draw()
        pygame.display.flip()

    def run(self):
        self.running = True

        while self.running:
            self.poll_events()
            self.update_scene()
            self.draw_scene()
        
        pygame.quit()
        self.logger.info("Goodbye!")
        exit(0)

