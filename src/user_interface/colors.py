# colors.py

from core.logger import get_logger

COLOR_BLACK = '#000000'
COLOR_GRAY = '#808080'
COLOR_RED = '#ff0000'

solarized =  {
    'base03':   '#002b36', # bg (darkest)
    'base02':   '#073642', # bg (lightest)
    'base01':   '#586e75', # gray (darkest)
    'base00':   '#657b83', # gray
    'base0':    '#839496', # gray
    'base1':    '#93a1a1', # gray (lightest)
    'base2':    '#eee8d5', # white (darkest)
    'base3':    '#fdf6e3', # white (lightest)
    'yellow':   '#b58900',
    'orange':   '#cb4b16',
    'red':      '#dc322f',
    'magenta':  '#d33682',
    'violet':   '#6c71c4',
    'blue':     '#268bd2', # darker blue
    'cyan':     '#2aa198',
    'green':    '#859900',
    'gray':     '#808080',
}

class GameColors:
    def __init__(self):
        self.logger = get_logger(__name__)

        # colors
        self.background = "#000000"
        self.button_idle = "#000000"
        self.button_hover = "#000000"
        self.button_click = "#000000"
        self.button_border = "#000000"
        self.text_dark = "#000000"
        self.text_light = "#000000"
        self.tile0 = "#000000"
        self.tile1 = "#000000"
        self.tile2 = "#000000"
        self.tile3 = "#000000"
        self.tile4 = "#000000"
        self.tile5 = "#000000"
        self.tile6 = "#000000"
        self.tile7 = "#000000"
        self.tile8 = "#000000"
        self.tile9 = "#000000"
        self.tile_wrong = "#000000"

        self.solarized_mapping = {
            "background"    : solarized["base02"],
            "button_idle"   : solarized["base01"],
            "button_hover"  : solarized["base00"],
            "button_click"  : solarized["base0"],
            "button_border" : COLOR_BLACK,
            
            "text_dark": COLOR_BLACK,
            "text_light": solarized["base2"],
            
            "tile0": COLOR_BLACK,
            "tile1": solarized["red"],
            "tile2": solarized["yellow"],
            "tile3": solarized["green"],
            "tile4": solarized["orange"],
            "tile5": solarized["cyan"],
            "tile6": solarized["blue"],
            "tile7": solarized["magenta"],
            "tile8": solarized["violet"],
            "tile9": solarized["gray"],
            "tile_wrong": COLOR_RED
        }

        self.grayscale_light_mapping = {
            "background"    : "#e0e0e0",
            "button_idle"   : "#a0a0a0",
            "button_hover"  : "#808080",
            "button_click"  : "#606060",
            "button_border" : "#000000",
            
            "text_dark": "#000000",
            "text_light": "#e0e0e0",
            
            "tile0": "#000000",
            "tile1": "#111111",
            "tile2": "#222222",
            "tile3": "#333333",
            "tile4": "#444444",
            "tile5": "#555555",
            "tile6": "#666666",
            "tile7": "#777777",
            "tile8": "#888888",
            "tile9": "#999999",
            "tile_wrong": "#ff0000"
        }
        
        #self.pastel_mapping = {
        #    
        #}

        self.colors = self.solarized_mapping

    def set_color_scheme(self, scheme: str):
        valid_schemes = ["solarized", "grayscale_light"]

        set_mapping = {
            "solarized": self.solarized_mapping, 
            "grayscale_light": self.grayscale_light_mapping,
        }

        if scheme not in valid_schemes:
            raise ValueError("{} not in valid_schemes: [{}]".format(
                scheme, ", ".join(valid_schemes)
            ))
            exit(1)

        color_mapping = set_mapping.get(scheme, "solarized")
        for color_name, color_string in color_mapping.items():
            if hasattr(self, color_name):
                setattr(self, "color_name", "color_string")
            else:
                self.logger.warning("Unknown color attribute {}".format(color_name))
                