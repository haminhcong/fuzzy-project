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

# Player module, the car.
import math
import pygame
from math import atan2, degrees, pi
import maps
from loader import load_image
from maps import MAP_NAVS

PI = 3.14

GRASS_SPEED = 0.715
GRASS_GREEN = 75
CENTER_X = -1
CENTER_Y = -1


# Rotate car.
def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


def calculate_angel(point_x, point_y, target_x, target_y):
    neg_dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    if neg_dir < 0:
        neg_dir += 360
    if neg_dir < 90:
        dir = neg_dir + 360 - 90
    else:
        dir = neg_dir - 90
    return dir


# define car as Player.

class Car(pygame.sprite.Sprite):
    # init_x, init_y: center of image
    def __init__(self, init_x, init_y, init_dir):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('car_player.png')
        self.rect = self.image.get_rect()
        self.rect_w = self.rect.size[0]
        self.rect_h = self.rect.size[1]
        self.image_orig = self.image
        self.screen = pygame.display.get_surface()
        self.area = self.screen.get_rect()
        self.x = init_x
        self.y = init_y
        self.rect.topleft = 600 - self.rect_w / 2, 300 - self.rect_h / 2

        self.dir = init_dir
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)
        self.speed = 0.0
        # self.maxspeed = 11.5
        self.maxspeed = 3
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.dir_factor = 0.05
        self.current_nav_index = 0

    def impact(self):
        if self.speed > 0:
            self.speed = self.minspeed

            # def soften(self):
            #     if self.speed > 0:
            #         self.speed -= self.softening
            #     if self.speed < 0:
            #         self.speed += self.softening

            # Accelerate the vehicle

    def accelerate(self):
        if self.speed < self.maxspeed:
            self.speed = self.speed + self.acceleration

    def stop(self):
        self.speed = 0

    def set_speed(self, speed):
        self.speed = speed

    def set_dir(self, way_dir):
        self.dir = way_dir
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)

    def deaccelerate(self):
        if self.speed > self.minspeed:
            self.speed = self.speed - self.deacceleration

    def steerleft(self):
        self.dir = self.dir + self.steering
        if self.dir > 360:
            self.dir = 0
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)

    # Steer.
    def steerright(self):
        self.dir = self.dir - self.steering
        if self.dir < 0:
            self.dir = 360
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)

    def find_way_direction(self):
        next_nav_index = self.current_nav_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        # print(str(self.x) + " : " + str(self.y) + " : " + str(
        #     next_nav_x) + " : " + str(next_nav_y))
        return calculate_angel(self.x, self.y, next_nav_x, next_nav_y)

    def find_new_dir(self, screen):
        max_dir_length = 0
        max_dir_way = self.dir
        max_coor_x = self.x
        max_coor_y = self.y
        for dir in range(int(self.dir) + MAX_RADAR_RIGHT_ANGLE,
                         int(self.dir) + MAX_RADAR_LEFT_ANGLE + 1):
            # print(dir)
            max_way_length = 0
            check_coor_x = self.x
            check_coor_y = self.y
            for distance in range(0, MAX_RADAR_RADIUS):
                check_coor_x = self.x + distance * math.cos(
                    math.radians(270 - dir))
                check_coor_y = self.y + distance * math.sin(
                    math.radians(270 - dir))
                try:
                    check_color = screen.get_at(
                        (int(check_coor_x), int(check_coor_y)))
                    if 160 < check_color.r < 190 \
                            and 160 < check_color.g < 190 \
                            and 160 < check_color.b < 190:
                        max_way_length += 1
                    else:
                        break
                except Exception as e:
                    pass

            if max_way_length > max_dir_length:
                max_dir_way = dir
                max_dir_length = max_way_length
                max_coor_x = check_coor_x
                max_coor_y = check_coor_y
        # print(max_dir_length)
        # print(max_coor_x)
        # print(max_coor_y)
        # print(
        #     str(self.x) + ":" + str(self.y) + ":" + str(max_dir_length) + ":" +
        #     str(max_dir_way))
        # print()
        return max_dir_way

    def update_map_nav_index(self):
        next_nav_index = self.current_nav_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        if (abs(self.x - next_nav_x) < self.maxspeed and
                    abs(self.y - next_nav_y) < self.maxspeed):
            self.current_nav_index = next_nav_index

    def change_dir(self, target_dir):
        next_nav_index = self.current_nav_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        distance_to_next_nav = math.sqrt(math.pow((self.x - next_nav_x), 2) + \
                                         math.pow(self.y - next_nav_y, 2))
        dir_before_change = str(self.dir - target_dir)
        if abs(self.dir - target_dir) > 2:
            # self.dir -= self.dir_factor * \
            #             float(self.dir - target_dir) * self.speed / \
            #             distance_to_next_nav
            if self.dir > target_dir:
                angle = self.dir_factor * float(self.dir - target_dir)
                change_dir = angle if angle < 2 else 2
                self.dir -= change_dir
            else:
                angle = self.dir_factor * float(target_dir - self.dir)
                change_dir = angle if angle < 2 else 2
                self.dir += change_dir
        dir_after_change = str(self.dir - target_dir)
        if (self.dir - target_dir)>10:
            print(
                "before change:" + dir_before_change +
                "- after change:" + dir_after_change)
        # print(str(self.dir) + " : " + str(target_dir))
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)

    def update_speed(self, target_dir):
        if abs(self.dir - target_dir) < 3:
            check_speed = 30 / abs(self.dir - target_dir)
            self.speed = check_speed if check_speed < 1 else 1
        else:
            self.speed = max(self.speed - 0.25, 0.25)

        # print("speed - " + str(self.speed))

    # fix this function
    def update(self, last_x, last_y):
        # print(str(self.x) + " : " + str(self.y))
        self.update_map_nav_index()
        if self.current_nav_index < maps.FINISH_INDEX:
            # calculate way direction
            way_dir = self.find_way_direction()
            self.change_dir(way_dir)
            # print(way_dir)
            self.update_speed(way_dir)
            # controlled_car.set_speed(2)
        else:
            self.set_speed(0)
        self.x = self.x + self.speed * math.cos(math.radians(270 - self.dir))
        self.y = self.y + self.speed * math.sin(math.radians(270 - self.dir))
