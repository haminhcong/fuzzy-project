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


class TrafficLamp(pygame.sprite.Sprite):
    # LAMP status
    GREEN = 1
    RED = 2
    YELLOW = 3

    # time out from lamp switch from GREEN to RED And backward
    TIMEOUT = 600

    LAMP_RED_IMG = None
    LAMP_GREEN_IMG = None
    LAMP_YELLOW_IMG = None

    def __init__(self, init_x, init_y, dir, status=None, remaining_time=None):
        self.LAMP_IMG = load_image('traffic_lamp.png')
        self.RED_RECT = ((0, 0), (41, 100))
        self.GREEN_RECT = ((42, 0), (42, 100))
        self.YELLOW_RECT = ((82, 0), (125, 100))
        pygame.sprite.Sprite.__init__(self)
        if status is not None and status != TrafficLamp.GREEN and \
                        status != TrafficLamp.YELLOW:
            raise Exception("init status of traffic lamp must be RED or GREEN")
        if status is None:
            status = random.randint(1, 2)
        if remaining_time is None:
            remaining_time = random.randint(60, 600)
        # previous status of traffic lamp
        self.prev_status = TrafficLamp.YELLOW
        # current status of traffic lamp
        self.status = status
        # time remaining before traffic lamp change status
        self.remaining_time = remaining_time
        # print(self.remaining_time)
        # traffic lamp position
        self.x = init_x
        self.y = init_y
        # traffic lamp direction (0,90,180,270)
        self.dir = dir
        # self.image = self.set_traffic_lamp_img()
        self.image = self.LAMP_IMG
        self.sprite_rect = self.set_traffic_lamp_img()
        self.rect = self.image.get_rect()
        # self.rect_w = self.rect.size[0]
        # self.rect_h = self.rect.size[1]
        self.rect.center = self.x, self.y

    def set_traffic_lamp_img(self):
        if self.status == TrafficLamp.RED:
            return self.RED_RECT
        elif self.status == TrafficLamp.GREEN:
            return self.GREEN_RECT
        elif self.status == TrafficLamp.YELLOW:
            return self.YELLOW_RECT

    def switch_status(self):
        if self.status == TrafficLamp.YELLOW:
            if self.prev_status == TrafficLamp.RED:
                self.prev_status = TrafficLamp.YELLOW
                self.status = TrafficLamp.GREEN
            else:
                self.prev_status = TrafficLamp.YELLOW
                self.status = TrafficLamp.RED
            self.remaining_time = 600

        elif self.status == TrafficLamp.RED:
            self.prev_status = TrafficLamp.RED
            self.status = TrafficLamp.YELLOW
            self.remaining_time = 60
        else:
            self.prev_status = TrafficLamp.GREEN
            self.status = TrafficLamp.YELLOW
            self.remaining_time = 60
        self.sprite_rect = self.set_traffic_lamp_img()
        # self.rect = self.image.get_rect()
        pass

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.center = self.x - cam_x + 600, self.y - cam_y + 300
        self.remaining_time -= 1
        if self.remaining_time == 0:
            self.switch_status()
            # print(self.rect.topleft)
            # print(str(cam_x)+" : "+str(cam_y))

    def render(self, screen):
        lamp_font = pygame.font.SysFont(None, 25)
        # render text
        label = lamp_font.render(str(int(self.remaining_time / 60)), 1,
                                 (255, 255, 255))
        screen.blit(label, (self.rect.center[0] + 60, self.rect.center[1]))
        screen.blit(self.image, (self.rect.topleft[0], self.rect.topleft[1]),
                    pygame.Rect(self.sprite_rect))
