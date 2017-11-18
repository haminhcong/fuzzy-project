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
from math import atan2, degrees, pi, sqrt
import maps
from traffic_lamp import TrafficLamp
from fuzzy_logic_engine import data_input, fuzzy_logic_engine
from loader import load_image
from maps import MAP_NAVS
from utils import calculate_angel, angle_diff, add_angle

PI = 3.14

GRASS_SPEED = 0.715
GRASS_GREEN = 75
CENTER_X = -1
CENTER_Y = -1


# Rotate car.
def rot_center(image, rect, angle):
    # print("angle: " + str(angle))
    # return image, rect
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image, rot_rect


# def calculate_angel(point_x, point_y, target_x, target_y):
#     neg_dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
#     if neg_dir < 0:
#         neg_dir += 360
#     if neg_dir < 90:
#         dir = neg_dir + 360 - 90
#     else:
#         dir = neg_dir - 90
#     return dir


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
        # self.rect.topleft = 600 - self.rect_w / 2, 300 - self.rect_h / 2
        self.rect.center = 600, 300
        self.dir = init_dir
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)
        self.speed = 0.0
        # self.maxspeed = 11.5
        self.maxspeed = 1.5
        self.minspeed = -1.85
        self.acceleration = 0.095
        self.deacceleration = 0.12
        self.softening = 0.04
        self.steering = 1.60
        self.dir_factor = 0.1
        # self.line_index = self.current_line_index
        self.current_line_index = 0  # index of current line in map which this car is in

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
        next_nav_index = self.current_line_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        # print(str(self.x) + " : " + str(self.y) + " : " + str(
        #     next_nav_x) + " : " + str(next_nav_y))
        return calculate_angel(self.x, self.y, next_nav_x, next_nav_y)

    def update_map_line_index(self):
        next_nav_index = self.current_line_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]
        if (abs(self.x - next_nav_x) < self.maxspeed and
                    abs(self.y - next_nav_y) < self.maxspeed):
            self.current_line_index = next_nav_index

    def change_dir(self, target_dir):
        # self.dir = target_dir
        next_nav_index = self.current_line_index + 1
        next_nav_x, next_nav_y = \
            MAP_NAVS[next_nav_index][0], MAP_NAVS[next_nav_index][1]

        if abs(angle_diff(self.dir, target_dir)) > 2:
            # print("car:" + str(self.dir) + " way: " + str(target_dir))
            # print("angle diff: " + str(angle_diff(self.dir, target_dir)))
            # self.dir -= self.dir_factor * \
            #             float(self.dir - target_dir) * self.speed / \
            #             distance_to_next_nav
            if angle_diff(self.dir, target_dir) >= 0:
                angle = self.dir_factor * \
                        float(angle_diff(self.dir, target_dir))
                if abs(angle < 4):
                    change_dir = angle
                elif angle > 4:
                    change_dir = 4
                else:
                    change_dir = -4
                self.dir = add_angle(self.dir, change_dir)
            else:
                angle = self.dir_factor * \
                        float(angle_diff(self.dir, target_dir))
                if abs(angle < 4):
                    change_dir = angle
                elif angle > 4:
                    change_dir = 4
                else:
                    change_dir = -4
                self.dir = add_angle(self.dir, change_dir)
                # print("after update: car:" + str(self.dir) + " way: " + str(
                #     target_dir))
        # print(str(self.dir) + " : " + str(target_dir))
        self.image, self.rect = rot_center(self.image_orig, self.rect,
                                           self.dir)

        # def update_speed(self, target_dir):
        #     if abs(angle_diff(self.dir, target_dir)) < 7:
        #         # check_speed = 30 / abs(self.dir - target_dir)
        #         check_speed = self.speed + 0.1
        #         self.speed = check_speed if check_speed < self.maxspeed else self.maxspeed
        #         # self.speed = check_speed if check_speed < 1 else 1
        #     else:
        #         self.speed = max(self.speed - 0.25, 0.25)

        # print("speed - " + str(self.speed))

    # fix this function
    def update(self, last_x, last_y, app):
        if not app.pause:
            # print(self.dir)
            if self.current_line_index < maps.FINISH_INDEX:
                way_dir = self.find_way_direction()
                barriers = app.barriers
                traffic_lamps = app.traffic_lamps
                ahead_thing = None
                lamp_state = None
                lamp_remain_time = None
                ahead_distance = -1
                for barrier in barriers:
                    check_distance = self.check_distance(
                        barrier.line_index, barrier.line_distance
                    )
                    if check_distance != -1 and \
                            (ahead_distance > check_distance or ahead_distance == -1):
                        ahead_distance = check_distance
                        ahead_thing = 'barrier'
                for traffic_lamp in traffic_lamps:
                    check_distance = self.check_distance(
                        traffic_lamp.line_index, traffic_lamp.line_distance
                    )
                    if check_distance != -1 and \
                            (ahead_distance > check_distance or ahead_distance == -1):
                        ahead_distance = check_distance
                        ahead_thing = data_input.TRAFFIC_LAMP
                        if traffic_lamp.status == TrafficLamp.RED:
                            lamp_state = data_input.LAMP_RED
                        if traffic_lamp.status == TrafficLamp.GREEN:
                            lamp_state = data_input.LAMP_GREEN
                        if traffic_lamp.status == TrafficLamp.YELLOW:
                            lamp_state = data_input.LAMP_YELLOW
                        lamp_remain_time = traffic_lamp.remaining_time
                # input: ahead_thing, ahead_distance, direction, lamp_status
                if ahead_thing is None:
                    ahead_thing = 'barrier'
                    ahead_distance = 1000
                diff_degree = abs(angle_diff(self.dir, way_dir))
                speed = fuzzy_logic_engine.set_speed(ahead_thing, ahead_distance, diff_degree,
                                                     lamp_state, lamp_remain_time)
                self.update_map_line_index()
                # calculate way direction
                self.change_dir(way_dir)
                self.set_speed(speed)
                # self.update_speed(way_dir)
                # controlled_car.set_speed(2)
            else:
                self.set_speed(0)
            self.x = self.x + self.speed * math.cos(math.radians(self.dir))
            self.y = self.y - self.speed * math.sin(math.radians(self.dir))

    def check_distance(self, thing_line_index, thing_line_distance):
        if self.current_line_index > thing_line_index:
            return -1
        elif self.current_line_index == thing_line_index:
            start_line_point = MAP_NAVS[self.current_line_index]
            current_distance = sqrt(pow(self.x - start_line_point[0], 2) +
                                    pow(self.y - start_line_point[1], 2))
            if current_distance < thing_line_distance:
                return thing_line_distance - current_distance
            else:
                return -1
        else:
            start_line_point = MAP_NAVS[self.current_line_index]
            current_distance = sqrt(pow(self.x - start_line_point[0], 2) +
                                    pow(self.y - start_line_point[1], 2))
            current_line_index = self.current_line_index
            current_line_length = Car.get_line_length(MAP_NAVS[current_line_index],
                                                      MAP_NAVS[current_line_index + 1])
            distance = current_line_length - current_distance
            current_line_index += 1
            while current_line_index < thing_line_index:
                distance += Car.get_line_length(MAP_NAVS[current_line_index],
                                                MAP_NAVS[current_line_index + 1])
                current_line_index += 1
            distance += thing_line_distance
            return distance

    @staticmethod
    def get_line_length(start_point, end_point):
        return sqrt(pow(end_point[0] - start_point[0], 2) +
                    pow(end_point[1] - start_point[1], 2))
