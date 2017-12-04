from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, DISTANCE_NEAR, DISTANCE_MEDIUM, DISTANCE_FAR
from ..fuzzy_info import DISTANCE_NEAR_FUZZY_INFO, DISTANCE_MEDIUM_FUZZY_INFO, \
    DISTANCE_FAR_FUZZY_INFO


# lamp truth_value
def calculate_near_truth_value(distance):
    if distance <= DISTANCE_NEAR_FUZZY_INFO[1]:
        return 1.0
    if DISTANCE_NEAR_FUZZY_INFO[1] < distance <= DISTANCE_NEAR_FUZZY_INFO[2]:
        return 1.0 * (DISTANCE_NEAR_FUZZY_INFO[2] - distance) / \
               (DISTANCE_NEAR_FUZZY_INFO[2] - DISTANCE_NEAR_FUZZY_INFO[1])
    else:
        return 0.0


def calculate_medium_truth_value(distance):
    if distance < DISTANCE_MEDIUM_FUZZY_INFO[1]:
        return 0.0
    elif DISTANCE_MEDIUM_FUZZY_INFO[1] <= distance < DISTANCE_MEDIUM_FUZZY_INFO[2]:
        return 1.0 * (distance - DISTANCE_MEDIUM_FUZZY_INFO[1]) / \
               (DISTANCE_MEDIUM_FUZZY_INFO[2] - DISTANCE_MEDIUM_FUZZY_INFO[1])
    elif DISTANCE_MEDIUM_FUZZY_INFO[2] <= distance <= DISTANCE_MEDIUM_FUZZY_INFO[3]:
        return 1.0
    elif DISTANCE_MEDIUM_FUZZY_INFO[3] <= distance <= DISTANCE_MEDIUM_FUZZY_INFO[4]:
        return 1.0 * (DISTANCE_MEDIUM_FUZZY_INFO[4] - distance) / \
               (DISTANCE_MEDIUM_FUZZY_INFO[4] - DISTANCE_MEDIUM_FUZZY_INFO[3])
    else:
        return 0.0


def calculate_far_truth_value(distance):
    if distance < DISTANCE_FAR_FUZZY_INFO[1]:
        return 0.0
    elif DISTANCE_FAR_FUZZY_INFO[1] <= distance < DISTANCE_FAR_FUZZY_INFO[2]:
        return 1.0 * (distance - DISTANCE_FAR_FUZZY_INFO[1]) / \
               (DISTANCE_FAR_FUZZY_INFO[2] - DISTANCE_FAR_FUZZY_INFO[1])

    else:
        return 1.0


def fuzzify_distance_value(distance):
    distance_fuzzy_list = []
    near_truth_value = \
        calculate_near_truth_value(distance)
    medium_truth_value = \
        calculate_medium_truth_value(distance)
    far_truth_value = \
        calculate_far_truth_value(distance)
    if near_truth_value > 0.0:
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_NEAR, near_truth_value))
    if medium_truth_value > 0.0:
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_MEDIUM, medium_truth_value))
    if far_truth_value > 0.0:
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_FAR, far_truth_value))
    return distance_fuzzy_list
