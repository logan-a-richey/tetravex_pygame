# base_scene.py

# abstract class
from abc import ABC, abstractmethod

class BaseScene:
    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def update(self): pass
    
    @abstractmethod
    def on_mouse_down(self): pass

    @abstractmethod
    def on_mouse_up(self): pass

    @abstractmethod
    def draw(self): pass

