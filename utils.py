import math
from math import pi as PI



def angle_diff(angle_x, angle_y):
    if abs(angle_y - angle_x) <= 180:
        return angle_y - angle_x
    else:
        if angle_y - angle_x >= 180:
            return angle_y - (angle_x + 360)
        else:
            return angle_y + 360 - angle_x


def add_angle(current_value, angel_changed):
    new_value = current_value + angel_changed
    if new_value < 0:
        new_value += 360
    elif new_value > 360:
        new_value -= 360
    return new_value


def calculate_angel(point_x, point_y, target_x, target_y):
    dir = math.atan2(point_y - target_y, target_x - point_x) * 180 / PI
    if dir < 0:
        dir += 360
    # if neg_dir < 0:
    #     neg_dir += 360
    # if neg_dir < 90:
    #     dir = neg_dir + 360 - 90
    # else:
    #     dir = neg_dir - 90
    return dir
