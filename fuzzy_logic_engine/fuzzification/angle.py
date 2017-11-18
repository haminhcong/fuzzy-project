from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, ANGLE_BIG, ANGLE_MEDIUM, ANGLE_SMALL


# lamp truth_value
def calculate_angle_small_truth_value(angle):
    if angle < 2:
        return 1.0
    if 2 <= angle <= 5:
        return (5 - angle) / 3.0
    else:
        return 0.0


def calculate_angle_medium_truth_value(angle):
    if angle < 3:
        return 0.0
    elif 3 <= angle <= 6:
        return (angle - 3) / 3.0
    elif 6 <= angle <= 9:
        return (9 - angle) / 3.0
    else:
        return 0.0


def calculate_angle_big_truth_value(angle):
    if angle < 8:
        return 0.0
    elif 8 <= angle <= 10:
        return (angle - 8) / 2.0
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
