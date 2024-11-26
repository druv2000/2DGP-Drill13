from pico2d import *
import game_world
import game_framework
import random

import server


class Ball:
    image = None

    def __init__(self, x=None, y=None):
        if Ball.image == None:
            Ball.image = load_image('ball21x21.png')
        self.x = x if x else random.randint(100, 1180)
        self.y = y if y else random.randint(100, 924)

    def draw(self):
        self.image.draw(self.cx, self.cy)
        draw_rectangle(*self.get_bb())

    def update(self):
        self.cx = self.x - server.background.window_left
        self.cy = self.y - server.background.window_bottom
        pass

    def get_bb(self):
        return self.cx - 10, self.cy - 10, self.cx + 10, self.cy + 10

    def handle_collision(self, group, other):
        if group == 'boy:ball':
            game_world.remove_object(self)
        pass
