# button.py

import pygame
from typing import Tuple

def nop():
    print("Button clicked!")

class Button:
    def __init__(self, manager,
        func=nop,
        text="Default", 
        text_color=(0,0,0),
        pos=(0,0), 
        dim=(200,100),
        color=(200,200,200)
    ):
        self.manager = manager
        
        self.text = text
        self.text_color = text_color

        # TODO render once method:
        # self.text = self.manager.font.render(text, True, text_color)
        
        self.color_idle = color
        self.color_hover = tuple([x * 0.8 for x in color])
        self.color_click = tuple([x * 0.6 for x in color])
        self.color = self.color_idle

        self.rect = pygame.Rect(*pos, *dim) 
        self.func = func

    def update(self):
        mouse_over = self.rect.collidepoint(self.manager.mouse_pos)
        
        self.color = self.color_idle
        if mouse_over:
            self.color = self.color_hover
            if self.manager.is_mouse_down:
                self.color = self.color_click
    
    def draw_text_center(self, 
        text: str, 
        pos: Tuple[int, int], 
        color: Tuple[int, int]
    ):
        text = self.manager.font.render(text, True, color)
        text_rect = text.get_rect(center=pos)
        self.manager.screen.blit(text, text_rect)

    def draw(self):
        pygame.draw.rect(self.manager.screen, self.color, self.rect)
        pygame.draw.rect(self.manager.screen, (0,0,0), self.rect, width=2)
        button_center = (self.rect.w // 2, self.rect.h // 2)
        self.draw_text_center(self.text, button_center, self.text_color)
    
    def on_mouse_up(self):
        mouse_over = self.rect.collidepoint(self.manager.mouse_pos)
        if mouse_over:
            self.func()

