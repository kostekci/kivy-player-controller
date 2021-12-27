import kivy
kivy.require('1.1.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty, BooleanProperty
)
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.core.window import Window



class Player(Widget):
    pass

class Game(Widget):
    player1 = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Game, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            self.player1.center_y += 25
        elif keycode[1] == 'down':
            self.player1.center_y -= 25
        elif keycode[1] == 'right':
            self.player1.center_x += 25
        elif keycode[1] == 'left':
            self.player1.center_x -= 25
        return True       

    def update(self, dt):
        pass


class GameApp(App):
    def build(self):
        game = Game()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    GameApp().run()
