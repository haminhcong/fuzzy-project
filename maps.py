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

import pygame
from loader import load_image

# Map filenames.
MAP_NAVS = [(600, 350), (690, 370), (810, 385), (910, 380), (1030, 345),
            (1120, 315), (1385, 325), (1540, 375), (1740, 450), (1890, 520),
            (2035, 565), (2230, 640), (2435, 685), (2585, 730), (2735, 790),
            (2840, 890), (2840, 1030), (2748, 1134), (2610, 1110),
            (2455, 1050),
            (2332, 1034), (2140, 1076), (1970, 1125), (1698, 1166),
            (1476, 1138),
            (1256, 1115), (1000, 1130), (756, 1205), (544, 1282), (458, 1398),
            (404, 1540), (410, 1585)]

FINISH_INDEX = 30


class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('map.png')
        self.rect = self.image.get_rect()
        self.x = init_x
        self.y = init_y

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 600, self.y - cam_y + 300
