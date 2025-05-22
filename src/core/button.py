# button.py

import pygame
from typing import Tuple

def nop():
    print("Button clicked!")

class Button:
    def __init__(self, manager,
        func=nop,
        text="Default", 
        text_color=(0, 0, 0),
        pos=(0, 0), 
        dim=(200, 100),
        color=(200, 200, 200)
    ):
        self.manager = manager
        self.func = func
        self.text = text
        self.text_color = text_color

        self.rect = pygame.Rect(*pos, *dim)

        # Color states
        self.color_idle = color
        self.color_hover = tuple([int(x * 0.8) for x in color])
        self.color_click = tuple([int(x * 0.6) for x in color])
        self.color = self.color_idle

        # Pre-render text surface and rect
        self.text_surface = self.manager.font.render(self.text, True, self.text_color)
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def update(self):
        mouse_over = self.rect.collidepoint(self.manager.mouse_pos)
        
        self.color = self.color_idle
        if mouse_over:
            self.color = self.color_hover
            if self.manager.is_mouse_down:
                self.color = self.color_click

    def draw(self):
        # Draw button
        pygame.draw.rect(self.manager.screen, self.color, self.rect)
        pygame.draw.rect(self.manager.screen, (0, 0, 0), self.rect, width=2)

        # Update text position in case the button moves
        self.text_rect.center = self.rect.center
        self.manager.screen.blit(self.text_surface, self.text_rect)

    def on_mouse_up(self):
        if self.rect.collidepoint(self.manager.mouse_pos):
            self.func()
