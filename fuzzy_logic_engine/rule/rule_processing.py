from . import read_rules

LAMP_RULES = read_rules.read_light_rule()
BARRIER_RULES = read_rules.read_barrier_rule()


def resolver_lamp_rule(distance_fuzzy_value, lamp_state_fuzzy_value, angle_fuzzy_value):
    for rule in LAMP_RULES:
        if distance_fuzzy_value.fuzzy_set_name == rule[0] and \
                        lamp_state_fuzzy_value.fuzzy_set_name == rule[1] and \
                        angle_fuzzy_value.fuzzy_set_name == rule[2]:
            truth_values = [distance_fuzzy_value.truth_value,
                            lamp_state_fuzzy_value.truth_value,
                            angle_fuzzy_value.truth_value]
            min_truth_value = min(truth_values)
            speed_fuzzy_set_name = rule[3]
            return speed_fuzzy_set_name, min_truth_value


def resolver_barrier_rule(distance_fuzzy_value, angle_fuzzy_value):
    for rule in BARRIER_RULES:
        if distance_fuzzy_value.fuzzy_set_name == rule[0] and \
                        angle_fuzzy_value.fuzzy_set_name == rule[1]:
            truth_values = [distance_fuzzy_value.truth_value,
                            angle_fuzzy_value.truth_value]
            min_truth_value = min(truth_values)
            speed_fuzzy_set_name = rule[2]
            return speed_fuzzy_set_name, min_truth_value
