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


class AddBarrierButton(pygame.sprite.Sprite):
    FAR = 'far'
    MEDIUM = 'medium'
    NEAR = 'near'

    def __init__(self, type, init_x, init_y, text):
        pygame.sprite.Sprite.__init__(self)
        # traffic lamp position
        self.x = init_x
        self.y = init_y
        self.text = text
        self.type = type
        self.image = load_image('barrier_' + self.type + '.png')
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.rect.topleft = self.x, self.y

    def update(self, cam_x, cam_y):
        pass

    def is_clicked(self, click_x, click_y):
        if self.x <= click_x <= self.x + self.rect_w \
                and self.y <= click_y <= self.y + self.rect_h:
            return True
        else:
            return False

    def render_text(self, screen):
        game_font = pygame.font.SysFont(None, 20)
        # render text
        label = game_font.render(self.text, 1,
                                 (40, 40, 40))
        label_rect = label.get_rect(
            center=(self.rect.topleft[0] + self.rect_w / 2,
                    self.rect.topleft[1] + self.rect_h / 2)
        )
        screen.blit(label,label_rect)

        # def handle_click(self, game):
