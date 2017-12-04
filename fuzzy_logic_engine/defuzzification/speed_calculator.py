import numpy as np
import skfuzzy

from fuzzy_logic_engine.fuzzification import fuzzy_value
from ..fuzzy_info import SPEED_DOMAIN_FUZZY_INFO as FUZZY_DOMAIN, \
    SPEED_FAST_FUZZY_INFO as FUZZY_FAST, SPEED_SLOW_FUZZY_INFO as FUZZY_SLOW, \
    SPEED_SLOWER_FUZZY_INFO as FUZZY_SLOWER, SPEED_STOP_FUZZY_INFO as FUZZY_STOP

# Trapezoidal
TRAPMF = 'trapezoidal'
# triangular
TRIMF = 'triangular'


class SpeedFuzzyFunction:
    def __init__(self, type, range, mark_points):
        self.type = type
        self.range = range
        self.mark_points = mark_points


# fast: from 1.5 to 2, 3
def defuzz_fast_speed(slice_value):
    speed_range = np.arange(FUZZY_DOMAIN[1], FUZZY_DOMAIN[2], 0.01)
    speed_high_fx = skfuzzy.trapmf(speed_range, [FUZZY_FAST[1], FUZZY_FAST[2],
                                                 FUZZY_FAST[3], FUZZY_FAST[4]])
    speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
    # check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
    defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'centroid')
    return defuzz_value


# slow: from 1 to 2
def defuzz_slow_speed(slice_value):
    speed_range = np.arange(FUZZY_DOMAIN[1], FUZZY_DOMAIN[2], 0.01)
    speed_high_fx = skfuzzy.trimf(speed_range, [FUZZY_SLOW[1], FUZZY_SLOW[2], FUZZY_SLOW[3]])
    speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
    # check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
    defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'centroid')
    return defuzz_value


# slower: from 0 to 1
def defuzz_slower_speed(slice_value):
    speed_range = np.arange(FUZZY_DOMAIN[1], FUZZY_DOMAIN[2], 0.01)
    speed_high_fx = skfuzzy.trimf(speed_range, [FUZZY_SLOWER[1], FUZZY_SLOWER[2], FUZZY_SLOWER[3]])
    speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
    # check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
    defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'centroid')
    return defuzz_value


# stop: from 0 to 0.5
def defuzz_stop_speed(slice_value):
    speed_range = np.arange(0, 3.001, 0.001)
    speed_high_fx = skfuzzy.trimf(speed_range, [FUZZY_STOP[1], FUZZY_STOP[2], FUZZY_STOP[3]])
    speed_high_active_slice = np.fmin(slice_value, speed_high_fx)
    # check_point = skfuzzy.interp_membership(speed_range, speed_high_active_slice, 1.375)
    defuzz_value = skfuzzy.defuzz(speed_range, speed_high_active_slice, 'mom')
    # if defuzz_value < 0.05:
    #     defuzz_value = 0
    # if defuzz_value == 0:
    #     print(defuzz_value)
    return defuzz_value


# slice value: value in vertical axis which slice line crossover
# this value == minimum value which found in calculation integrate value step
def defuzz_speed(init_speed_fuzzy_set, slice_value):
    if init_speed_fuzzy_set == fuzzy_value.SPEED_FAST:
        return defuzz_fast_speed(slice_value)

    elif init_speed_fuzzy_set == fuzzy_value.SPEED_SLOW:
        return defuzz_slow_speed(slice_value)

    elif init_speed_fuzzy_set == fuzzy_value.SPEED_SLOWER:
        return defuzz_slower_speed(slice_value)

    elif init_speed_fuzzy_set == fuzzy_value.SPEED_STOP:
        return defuzz_stop_speed(slice_value)

    else:
        raise Exception("Out of speed fuzzy set valid values.")
