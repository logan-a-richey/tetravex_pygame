# game_manager.py

import os
import warnings
from typing import Tuple, List, Dict, Union

# hide pygame warnings
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"

# hide pygame warnings
warnings.filterwarnings(
    "ignore",
    message="Your system is avx2 capable.*",
    category=RuntimeWarning
)

import pygame

# project imports
from core.logger import get_logger
from scenes.base_scene import BaseScene
from scenes.title_scene import TitleScene
from scenes.gameplay_scene import GameplayScene
from user_interface.colors import GameColors

class GameManager:
    ''' Controls game state and logic '''

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
        self.current_scene: Union[BaseScene, None] = TitleScene(self)
        self._pending_scene: Union[BaseScene, None] = None

        # set color theme
        self.color_picker = GameColors()
        self.color_scheme = self.color_picker.colors

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

    def change_scene(self, scene_name: str, *args, **kwargs):
        if scene_name == "title_scene":
            self._pending_scene = TitleScene(self)
        elif scene_name == "gameplay_scene":
            board_size = kwargs.get("board_size", 3)
            self._pending_scene = GameplayScene(self, board_size)
        elif scene_name == "exit":
            self.running = False
        else:
            self.logger.error("Invalid scene name {}. Exiting program".format(scene_name))
            exit(1)
    
    def update_scene(self):
        if self._pending_scene:
            self.current_scene = self._pending_scene
        
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

