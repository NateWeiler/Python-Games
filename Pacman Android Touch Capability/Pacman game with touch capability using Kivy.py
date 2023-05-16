# Pacman game with touch capability using Kivy

import kivy
kivy.require('1.11.1')

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, Line, Ellipse
from kivy.clock import Clock
from kivy.core.window import Window

# Set the window size
Window.size = (400, 400)

class PacmanGame(Widget):
# Initialize the game properties
def __init__(self, **kwargs):
super(PacmanGame, self).__init__(**kwargs)

self.dx = 0
self.dy = 0
self.stepCount = 0
self.pacmanMoving = False
self.pacmanSize = 30

self.GAME_SPEED = 0.1

self.xPos = 50
self.yPos = 50

with self.canvas:
self.pacman = Ellipse(pos=(self.xPos, self.yPos), size=(self.pacmanSize, self.pacmanSize), source='pacman.png')

# Create a keyboard listener for movement
self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
self._keyboard.bind(on_key_down=self._on_keyboard_down)

# Start the game clock
Clock.schedule_interval(self.update, self.GAME_SPEED)

# Update the game properties
def update(self, dt):
self.xPos += self.dx
self.yPos += self.dy

self.pacman.pos = (self.xPos, self.yPos)

self.stepCount += 1

if self.stepCount > 20:
self.pacmanMoving = False
self.stepCount = 0

# Close the keyboard listener
def _keyboard_closed(self):
self._keyboard.unbind(on_key_down=self._on_keyboard_down)
self._keyboard = None

# Handle the keyboard input
def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
if keycode[1] == 'left':
self.dx = -self.pacmanSize
self.dy = 0
self.pacmanMoving = True
elif keycode[1] == 'right':
self.dx = self.pacmanSize
self.dy = 0
self.pacmanMoving = True
elif keycode[1] == 'down':
self.dy = -self.pacmanSize
self.dx = 0
self.pacmanMoving = True
elif keycode[1] == 'up':
self.dy = self.pacmanSize
self.dx = 0
self.pacmanMoving = True

# Handle touch events for movement
def on_touch_down(self, touch):
if touch.x < self.xPos:
self.dx = -self.pacmanSize
self.dy = 0
self.pacmanMoving = True
elif touch.x > self.xPos:
self.dx = self.pacmanSize
self.dy = 0
self.pacmanMoving = True
elif touch.y < self.yPos:
self.dy = -self.pacmanSize
self.dx = 0
self.pacmanMoving = True
elif touch.y > self.yPos:
self.dy = self.pacmanSize
self.dx = 0
self.pacmanMoving = True

def on_touch_move(self, touch):
pass

def on_touch_up(self, touch):
self.pacmanMoving = False

class PacmanApp(App):
def build(self):
return PacmanGame()

if __name__ == '__main__':
PacmanApp().run()
