# The MIT License (MIT)

# Copyright (c) 2012 Robin Duda, (chilimannen)

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

# Camera module will keep track of sprite offset.

# Map file.
import math
import random
import pygame
from loader import load_image


class Barrier(pygame.sprite.Sprite):
    FAR_DISTANCE_RAND = (400, 1000)
    MEDIUM_DISTANCE_RAND = (200, 600)
    NEAR_DISTANCE_RAND = (80, 300)

    def __init__(self, line_index, line_distance, init_x, init_y, direction=None, remaining_time=None):
        pygame.sprite.Sprite.__init__(self)
        if remaining_time is None:
            remaining_time = random.randint(600, 1800)
        self.remaining_time = remaining_time
        # traffic lamp position
        self.line_index = line_index
        self.line_distance = line_distance
        self.x = init_x
        self.y = init_y
        # traffic lamp direction (0,90,180,270)
        self.dir = direction
        self.image = load_image('barrier.png')
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.rect.center = self.x, self.y

    def update(self, cam_x, cam_y):
        self.rect.center = self.x - cam_x + 600, self.y - cam_y + 300
        if self.remaining_time > 0:
            self.remaining_time -= 1

    def render_text(self, screen):
        game_font = pygame.font.SysFont(None, 25)
        # render text
        # color = (0, 0, 0)
        # pygame.draw.circle(screen, color, self.rect.center, 10)
        label = game_font.render(str(int(self.remaining_time / 60)), 1,
                                 (255, 255, 255))
        screen.blit(label, (self.rect.center[0] + 30, self.rect.center[1]))
