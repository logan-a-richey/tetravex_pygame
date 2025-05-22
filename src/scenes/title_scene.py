# title_scene.py

from scenes.base_scene import BaseScene
from core.button import Button

class TitleScene(BaseScene):
    def __init__(self, manager):
        self.manager = manager

        # objects in scene
        # TODO
        # title text: "Tetravex"
        pos = (50,50)
        dim = (300,100)

        self.buttons = [
            Button(
                self.manager, 
                func=self.handle_play, 
                text="Play", 
                pos=pos, 
                dim=dim,
                color=(0,200,200)
            )
        ]

        # button: Play
        # button: Highscore
        # button: Option
        # button: Quit
        pass

    def handle_play(self):
        print("Go to Gameplay scene")

    def update(self):
        for b in self.buttons:
            b.update()

    def on_mouse_down(self):
        pass

    def on_mouse_up(self):
        for b in self.buttons:
            b.on_mouse_up()

    def draw(self):
        for b in self.buttons:
            b.draw()

