from fuzzy_logic_engine.data_input import LAMP_GREEN, LAMP_RED, LAMP_YELLOW
from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, RED_FUZZY_SET, LESS_RED_FUZZY_SET, YELLOW_FUZZY_SET, \
    GREEN_FUZZY_SET, LESS_GREEN_FUZZY_SET

from ..fuzzy_info import RED_FUZZY_INFO, LESS_RED_FUZZY_INFO, YELLOW_FUZZY_INFO, \
    LESS_GREEN_FUZZY_INFO, GREEN_FUZZY_INFO


# lamp truth_value
# remaining_time: in tick (1/60s)
# red fuzzy_function:
def calculate_red_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_RED:
        if remaining_time >= RED_FUZZY_INFO[1]:
            return 1.0
        else:
            return 1.0 * remaining_time / RED_FUZZY_INFO[1]
    else:
        return 0.0


def calculate_less_red_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_RED:
        if remaining_time <= LESS_RED_FUZZY_INFO[1]:
            return 1.0
        elif LESS_RED_FUZZY_INFO[1] < remaining_time <= LESS_RED_FUZZY_INFO[2]:
            return 1.0 * (LESS_RED_FUZZY_INFO[2] - remaining_time) / \
                   (LESS_RED_FUZZY_INFO[2] - LESS_RED_FUZZY_INFO[1])
        else:
            return 0.0
    else:
        return 0.0


def calculate_yellow_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_YELLOW:
        return 1.0
    else:
        return 0.0


def calculate_less_green_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_GREEN:
        if remaining_time <= LESS_GREEN_FUZZY_INFO[1]:
            return 1.0
        elif LESS_GREEN_FUZZY_INFO[1] < remaining_time <= LESS_GREEN_FUZZY_INFO[2]:
            return 1.0 * (LESS_GREEN_FUZZY_INFO[2] - remaining_time) / \
                   (LESS_GREEN_FUZZY_INFO[2]-LESS_GREEN_FUZZY_INFO[1])
        else:
            return 0.0
    else:
        return 0.0


def calculate_green_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_GREEN:
        if remaining_time >= GREEN_FUZZY_INFO[1]:
            return 1.0
        else:
            return 1.0 * remaining_time / GREEN_FUZZY_INFO[1]
    else:
        return 0.0


def fuzzify_lamp_state_value(lamp_state, remaining_time):
    lamp_state_fuzzy_list = []
    red_truth_value = \
        calculate_red_truth_value(lamp_state, remaining_time)
    less_red_truth_value = \
        calculate_less_red_truth_value(lamp_state, remaining_time)
    yellow_truth_value = \
        calculate_yellow_truth_value(lamp_state, remaining_time)
    less_green_truth_value = \
        calculate_less_green_truth_value(lamp_state, remaining_time)
    green_truth_value = \
        calculate_green_truth_value(lamp_state, remaining_time)
    if red_truth_value > 0.0:
        lamp_state_fuzzy_list.append(FuzzyValue(RED_FUZZY_SET, red_truth_value))
    if less_red_truth_value > 0.0:
        lamp_state_fuzzy_list.append(FuzzyValue(LESS_RED_FUZZY_SET, less_red_truth_value))
    if yellow_truth_value > 0.0:
        lamp_state_fuzzy_list.append(FuzzyValue(YELLOW_FUZZY_SET, yellow_truth_value))
    if less_green_truth_value > 0.0:
        lamp_state_fuzzy_list.append(FuzzyValue(LESS_GREEN_FUZZY_SET, less_green_truth_value))
    if green_truth_value > 0.0:
        lamp_state_fuzzy_list.append(FuzzyValue(GREEN_FUZZY_SET, green_truth_value))
    return lamp_state_fuzzy_list
