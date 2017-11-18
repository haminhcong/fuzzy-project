from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, DISTANCE_NEAR, DISTANCE_MEDIUM, DISTANCE_FAR


# lamp truth_value
def calculate_near_truth_value(distance):
    if distance <= 200:
        return 1.0
    if 200 < distance <= 300:
        return 1.0 * (300 - distance) / 100
    else:
        return 0.0


def calculate_medium_truth_value(distance):
    if distance < 200:
        return 0.0
    elif 200 <= distance < 300:
        return 1.0 * (distance - 200) / 100
    elif 300 <= distance <= 500:
        return 1.0
    elif 500 <= distance <= 600:
        return 1.0 * (600 - distance) / 100
    else:
        return 0.0


def calculate_far_truth_value(distance):
    if distance < 300:
        return 0.0
    elif 300 <= distance < 800:
        return 1.0 * (distance - 300) / 500
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
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_NEAR,near_truth_value ))
    if medium_truth_value > 0.0:
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_MEDIUM, medium_truth_value))
    if far_truth_value > 0.0:
        distance_fuzzy_list.append(FuzzyValue(DISTANCE_FAR, far_truth_value))
    return distance_fuzzy_list
