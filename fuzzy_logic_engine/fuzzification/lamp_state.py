from fuzzy_logic_engine.data_input import LAMP_GREEN, LAMP_RED, LAMP_YELLOW
from fuzzy_logic_engine.fuzzification.fuzzy_value \
    import FuzzyValue, RED_FUZZY_SET, LESS_RED_FUZZY_SET, YELLOW_FUZZY_SET, \
    GREEN_FUZZY_SET, LESS_GREEN_FUZZY_SET


# lamp truth_value
# remaining_time: in tick (1/60s)
# red fuzzy_function:
def calculate_red_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_RED:
        if remaining_time >= 300:
            return 1.0
        else:
            return 1.0 * remaining_time / 300
    else:
        return 0.0


def calculate_less_red_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_RED:
        if remaining_time <= 200:
            return 1.0
        elif 200 < remaining_time <= 600:
            return 1.0 * (600 - remaining_time) / 400
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
        if remaining_time <= 300:
            return 1.0
        elif 300 < remaining_time <= 600:
            return 1.0 * (600 - remaining_time) / 300
        else:
            return 0.0
    else:
        return 0.0


def calculate_green_truth_value(lamp_state, remaining_time):
    if lamp_state == LAMP_GREEN:
        if remaining_time >= 600:
            return 1.0
        else:
            return 1.0 * remaining_time / 600
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
