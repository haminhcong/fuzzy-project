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
import random
import math
from math import pi as PI, sqrt
from loader import load_image
from barrier import Barrier
from button import AddBarrierButton
from utils import calculate_angel

# Map filenames.
MAP_NAVS = [(600, 350), (690, 370), (810, 385), (910, 380), (1030, 345),
            (1120, 315), (1385, 325), (1540, 375), (1740, 450), (1890, 520),
            (2035, 565), (2230, 640), (2435, 685), (2585, 730), (2735, 790),
            (2840, 890), (2840, 1030), (2748, 1134), (2610, 1110),
            (2455, 1050),
            (2332, 1034), (2140, 1076), (1970, 1125), (1698, 1166),
            (1476, 1138),
            (1256, 1115), (1000, 1130), (756, 1205), (544, 1282), (458, 1398),
            (404, 1540),(410, 1530)]

total_points = len(MAP_NAVS)

MAP_LINES = []


class MapLines:
    def __init__(self, index, start, end):
        self.index = index
        self.start = start
        self.end = end
        self.length = sqrt(pow(self.end[0] - self.start[0], 2) +
                           pow(self.end[1] - self.start[1], 2))


for i in range(0, total_points - 1):
    MAP_LINES.append(MapLines(i, MAP_NAVS[i], MAP_NAVS[i + 1]))

FINISH_INDEX = 30


class Map(pygame.sprite.Sprite):
    def __init__(self, init_x, init_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image('map.png')
        self.map_navs = MAP_NAVS
        self.rect = self.image.get_rect()
        self.x = init_x
        self.y = init_y

    # Realign the map
    def update(self, cam_x, cam_y):
        self.rect.topleft = self.x - cam_x + 600, self.y - cam_y + 300

    @staticmethod
    def find_random_barrier_pos(barrier_type, current_pos_index, current_pos):
        barrier_distance = 0
        # current_pos_index = x  mean that current car is between
        #  MAP_NAVS[x] and MAP_NAVS[x+1]
        if current_pos_index > FINISH_INDEX - 7:
            print("Current car will reach finish in short time, "
                  "stop creating barrier.")
            return None, None, None
        else:
            if barrier_type == AddBarrierButton.FAR:
                barrier_distance = random.randint(
                    Barrier.FAR_DISTANCE_RAND[0],
                    Barrier.FAR_DISTANCE_RAND[1])
            elif barrier_type == AddBarrierButton.MEDIUM:
                barrier_distance = random.randint(
                    Barrier.MEDIUM_DISTANCE_RAND[0],
                    Barrier.MEDIUM_DISTANCE_RAND[1])

            elif barrier_type == AddBarrierButton.NEAR:
                barrier_distance = random.randint(
                    Barrier.NEAR_DISTANCE_RAND[0],
                    Barrier.NEAR_DISTANCE_RAND[1])
            print(barrier_type + ":" + str(barrier_distance))

            current_distance = 0
            checked_distance = 0
            for i in range(0, 7):
                if i == 0:
                    check_line = (current_pos, MAP_NAVS[current_pos_index + 1])
                else:
                    check_line = (MAP_NAVS[current_pos_index + i],
                                  MAP_NAVS[current_pos_index + i + 1])
                barrier_target_pos, remain_distance = get_point_with_distance(
                    barrier_distance, checked_distance, check_line)
                if barrier_target_pos is not False:
                    barrier_index = current_pos_index + i
                    return barrier_index, remain_distance, barrier_target_pos,
                else:
                    checked_distance += get_line_length(check_line)
        return None


# start point: line[0], endpoint: line[1]
def get_line_length(line):
    start_point = line[0]
    end_point = line[1]
    return sqrt(pow(end_point[0] - start_point[0], 2) +
                pow(end_point[1] - start_point[1], 2))


# def calculate_angel(point_x, point_y, target_x, target_y):
#     neg_dir = math.atan2(target_y -point_y, target_x - point_x) * 180 / PI
#     if neg_dir < 0:
#         neg_dir += 360
#     if neg_dir < 90:
#         dir = neg_dir + 360 - 90
#     else:
#         dir = neg_dir - 90
#     return dir




# k = calculate_angel(0,0,0,-3)
# print(k)
pass


def get_point_with_distance(target_distance, checked_distance, check_line):
    line_length = get_line_length(check_line)
    remain_distance = target_distance - checked_distance
    # print("line length: " + str(line_length) + " - " +
    #       "remain distance length: " + str(remain_distance))
    if remain_distance > line_length:
        return False, remain_distance
    start_point = check_line[0]
    end_point = check_line[1]
    line_direction = calculate_angel(start_point[0], start_point[1],
                                     end_point[0], end_point[1])
    # print("start_point: " + str(start_point) + " - " +
    #       "end_point: " + str(end_point) + " - " +
    #       "line angle: " + str(line_direction))
    # print("")
    barrier_x = start_point[0] + \
                remain_distance * math.cos(math.radians(line_direction))
    barrier_y = start_point[1] - \
                remain_distance * math.sin(math.radians(line_direction))
    barrier_pos = (int(barrier_x), int(barrier_y))
    print("found barrier  point: " + str(barrier_pos))
    return barrier_pos, remain_distance


# line_index: index of line which put this lamp
# distance: distance from start point of line to lamp position
def find_lamp_pos(line_index, distance):
    check_line = MAP_LINES[line_index]
    if distance + 20 >= check_line.length:
        return None
    else:
        start_point = check_line.start
        end_point = check_line.end
        remain_distance = distance
        line_direction = calculate_angel(start_point[0], start_point[1],
                                         end_point[0], end_point[1])
        # print("start_point: " + str(start_point) + " - " +
        #       "end_point: " + str(end_point) + " - " +
        #       "line angle: " + str(line_direction))
        # print("")
        pos_x = start_point[0] + \
                remain_distance * math.cos(math.radians(line_direction))
        pos_y = start_point[1] - \
                remain_distance * math.sin(math.radians(line_direction))
        target_pos = (int(pos_x), int(pos_y))
        # print("found barrier  point: " + str(barrier_pos))
        return target_pos
