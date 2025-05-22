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
from user_interface.colors import GameColors

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

        # fonts
        self.font = pygame.font.SysFont(None, 36)
        
        # mouse
        self.mouse_pos: Tuple[int, int] = (0,0)
        self.is_mouse_down: bool = False
        
        # game specific
        self.running: bool = False
        self.current_scene: BaseScene = TitleScene(self)

        # set color theme
        self.color_picker = GameColors()
        self.color_scheme = self.color_picker.colors

    def change_scene(self, scene_string: str):
        valid_scenes = ["title", "gameplay"]
        if scene_string not in valid_scenes:
            self.logger.error("\'{}\' not in valid_scenes = [{}]".format(
                scene_string,
                ", ".format(valid_scenes)
            ))
            exit(1)
        
        if scene_string == "title":
            self.current_scene = TitleScene(self)
        elif scene_string == "gameplay":
            self.current_scene = GameplayScene(self)
        
    def on_mouse_down(self):
        self.is_mouse_down = True
        self.current_scene.on_mouse_down()

    def on_mouse_up(self):
        self.is_mouse_down = False
        self.current_scene.on_mouse_up()

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

