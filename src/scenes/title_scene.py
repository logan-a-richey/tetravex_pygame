# title_scene.py

import pygame

from typing import List, Tuple

from scenes.base_scene import BaseScene
from core.button import Button

class TitleScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager
        
        
        self.buttons: List[Button] = [
            Button(self.manager, func=lambda: self.manager.change_scene("gameplay_scene", board_size=3), text="Play"),
            Button(self.manager, func=lambda: self.manager.change_scene("exit"), text="Exit"),
        ]
        
        margin = 50
        button_w, button_h = 400, 100

        for i, button in enumerate(self.buttons):
            button.rect.x = margin
            button.rect.y = margin + (i * (margin + button_h))
            button.rect.w = button_w
            button.rect.h = button_h
        
        num_buttons = len(self.buttons)
        screen_dim = (
            margin * 2 + button_w,
            margin * 2 + (num_buttons * (button_h + margin) )
        )

        self.manager.screen = pygame.display.set_mode(screen_dim)
        
        # button: Play
        # TODO
        # button: Highscore
        # button: Option
        # button: Quit
        pass

    def update(self):
        for b in self.buttons:
            b.update()

    def on_mouse_down(self):
        pass

    def on_mouse_up(self):
        for b in self.buttons:
            b.on_mouse_up()

    def draw(self):
        # background
        self.manager.screen.fill("#404040")

        # buttons
        for b in self.buttons:
            b.draw()

