from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, ANGLE_BIG, ANGLE_MEDIUM, ANGLE_SMALL
from ..fuzzy_info import ANGLE_BIG_FUZZY_INFO, ANGLE_MEDIUM_FUZZY_INFO, \
    ANGLE_SMALL_FUZZY_INFO


# lamp truth_value
def calculate_angle_small_truth_value(angle):
    if angle < ANGLE_SMALL_FUZZY_INFO[1]:
        return 1.0
    if ANGLE_SMALL_FUZZY_INFO[1] <= angle <= ANGLE_SMALL_FUZZY_INFO[2]:
        return (ANGLE_SMALL_FUZZY_INFO[2] - angle) / \
               (ANGLE_SMALL_FUZZY_INFO[2] - ANGLE_SMALL_FUZZY_INFO[1])
    else:
        return 0.0


def calculate_angle_medium_truth_value(angle):
    if angle < ANGLE_MEDIUM_FUZZY_INFO[1]:
        return 0.0
    elif ANGLE_MEDIUM_FUZZY_INFO[1] <= angle <= ANGLE_MEDIUM_FUZZY_INFO[2]:
        return (angle - ANGLE_MEDIUM_FUZZY_INFO[1]) / \
               (ANGLE_MEDIUM_FUZZY_INFO[2] - ANGLE_MEDIUM_FUZZY_INFO[1])
    elif ANGLE_MEDIUM_FUZZY_INFO[2] <= angle <= ANGLE_MEDIUM_FUZZY_INFO[3]:
        return (ANGLE_MEDIUM_FUZZY_INFO[3] - angle) / \
               (ANGLE_MEDIUM_FUZZY_INFO[3] - ANGLE_MEDIUM_FUZZY_INFO[2])
    else:
        return 0.0


def calculate_angle_big_truth_value(angle):
    if angle < ANGLE_BIG_FUZZY_INFO[1]:
        return 0.0
    elif ANGLE_BIG_FUZZY_INFO[1] <= angle <= ANGLE_BIG_FUZZY_INFO[2]:
        return (angle - ANGLE_BIG_FUZZY_INFO[1]) / \
               (ANGLE_BIG_FUZZY_INFO[2] - ANGLE_BIG_FUZZY_INFO[1])
    else:
        return 1.0


def fuzzify_angle_value(angle):
    angle_fuzzy_list = []
    small_truth_value = \
        calculate_angle_small_truth_value(angle)
    medium_truth_value = \
        calculate_angle_medium_truth_value(angle)
    big_truth_value = \
        calculate_angle_big_truth_value(angle)
    if small_truth_value > 0.0:
        angle_fuzzy_list.append(FuzzyValue(ANGLE_SMALL, small_truth_value))
    if medium_truth_value > 0.0:
        angle_fuzzy_list.append(FuzzyValue(ANGLE_MEDIUM, medium_truth_value))
    if big_truth_value > 0.0:
        angle_fuzzy_list.append(FuzzyValue(ANGLE_BIG, big_truth_value))
    return angle_fuzzy_list
